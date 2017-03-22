import math


class Heap:
    """A heap - the base for heapsort, priority queues and such.
        This is a MIN heap. The head is the smallest element.
        i.e. one for which key(el) is the smallest
    """

    def __init__(self, *args, key=lambda arg: arg):
        self.__arr = []
        self.__arr.extend(args)
        self.key = key
        Heap.heapify(self.__arr, key=self.key)

    def get_min(self):
        return self.__arr[0]

    def extract_min(self):
        toreturn = self.__arr[0]
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        Heap.__sift(0, self.__arr, key=self.key)
        return toreturn

    def add(self, x):
        self.__arr.append(x)
        a = self.__arr

        def k(ind):
            return self.key(a[ind])

        i = len(a) - 1
        while Heap.parent(i) >= 0 and k(i) < k(Heap.parent(i)):
            a[i], a[Heap.parent(i)] = a[Heap.parent(i)], a[i]
            i = Heap.parent(i)

    def add_all(self, smth):
        if len(smth) > len(self.__arr) / math.log2(len(self.__arr)):
            self.__arr.extend(smth)
            Heap.heapify(self.__arr, key=self.key)
        else:
            for x in smth:
                self.add(x)

    @staticmethod
    def heapify(arr, key=lambda arg: arg):
        # nr_levels = math.ceil(math.log2(len(arr)+1))
        # find the parent of the last node, i.e. the last parent:
        start_index = Heap.parent(len(arr)-1)
        for n in range(start_index, -1, -1):
            Heap.__sift(n, arr, key=key)
        return arr

    @staticmethod
    def __sift(n, arr, key=lambda arg: arg):
        def intkey(i):
            return key(arr[i])
        while tuple(x for x in Heap.children(n, len(arr)) if intkey(n) > intkey(x)):
            min_child = min(list(Heap.children(n, len(arr))), key=intkey)
            arr[n], arr[min_child] = arr[min_child], arr[n]
            n = min_child

    @staticmethod
    def parent(n):
        if n > 0:
            return (n-1)//2
        else:
            return -1

    @staticmethod
    def children(n, l):
        return (x for x in (2*n+1, 2*n+2) if x < l)
