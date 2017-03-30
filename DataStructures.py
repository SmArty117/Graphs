import math


class Heap:
    """A heap - the base for heapsort, priority queues and such.
        This is a MIN heap. The head is the smallest element.
        i.e. one for which key(el) is the smallest
    """

    def __init__(self, arr, key=lambda arg: arg):
        self.__arr = []
        self.__arr.extend(arr)
        self.key = key
        Heap.heapify(self.__arr, key=self.key)

    def get_min(self):
        return self.__arr[0]

    def extract_min(self):
        toreturn = self.__arr[0]
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        self.__arr = self.__arr[:-1]
        Heap._sift(0, self.__arr, key=self.key)
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
        return i

    def add_all(self, iterable):
        if len(iterable) > len(self.__arr) / math.log2(len(self.__arr)):
            self.__arr.extend(iterable)
            Heap.heapify(self.__arr, key=self.key)
        else:
            for x in iterable:
                self.add(x)

    def emtpy(self):
        return len(self.__arr) == 0

    @staticmethod
    def heapify(arr, key=lambda arg: arg):
        # nr_levels = math.ceil(math.log2(len(arr)+1))
        # find the parent of the last node, i.e. the last parent:
        start_index = Heap.parent(len(arr)-1)
        for n in range(start_index, -1, -1):
            Heap._sift(n, arr, key=key)
        return arr

    @staticmethod
    def _sift(n, arr, key=lambda arg: arg):
        def intkey(i):
            return key(arr[i])
        while tuple(x for x in Heap.children(n, len(arr)) if intkey(n) > intkey(x)):
            min_child = min(list(Heap.children(n, len(arr))), key=intkey)
            arr[n], arr[min_child] = arr[min_child], arr[n]
            n = min_child
        return n

    @staticmethod
    def parent(n):
        if n > 0:
            return (n-1)//2
        else:
            return -1

    @staticmethod
    def children(n, l):
        return (x for x in (2*n+1, 2*n+2) if x < l)


def heapsort(arr, key=lambda arg: arg):
    """Returns an iterator through the sorted elements of arr
        Sorting occurs by the natural order of key(arr[i])
        Not guaranteed to be stable!
    """
    h = Heap(arr, key=key)
    while not h.emtpy():
        yield h.extract_min()


class PriorityQueue(Heap):
    """A queue in which items are sorted by priority.
        Uses an underlying heap representation.
    """

    def __init__(self, arr, key=lambda arg: arg):
        # insert values into the queue, but insert (key(v), v) into the heap
        Heap.__init__(self,
                      [(key(v), v) for v in arr],
                      key=lambda arg: arg[0])
        self.__arr = self._Heap__arr    # just a shorthand
        self._index = {c[1]: i for i, c in enumerate(self.__arr)}

    def push(self, x, *args):
        # if there is a priority specified, use that
        # if not, use the key(x) ?? is this a good idea?
        self._index[x] = Heap.add(self, (self.key(x), x))

    def decrease_key(self, item, new_key):
        del self.__arr[self._index[item]]
        del self._index[item]
        self.add((new_key, item))
