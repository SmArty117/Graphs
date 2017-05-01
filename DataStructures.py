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
        """Extract the root of the heap and return it"""

        toreturn = self.__arr[0]
        self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
        self.__arr = self.__arr[:-1]
        Heap._sift(0, self.__arr, key=self.key)
        return toreturn

    def add(self, x):
        """Add an element to the heap
            Returns the final index of the element if successful
        """
        self.__arr.append(x)
        return Heap._move_up(len(self.__arr)-1, self.__arr, key=self.key)

    def add_all(self, iterable):
        if len(iterable) > int(len(self.__arr) * (math.exp(len(self.__arr) - len(self.__arr)))):
            self.__arr.extend(iterable)
            Heap.heapify(self.__arr, key=self.key)
        else:
            for x in iterable:
                self.add(x)

    def __bool__(self):
        return bool(self.__arr)

    def __contains__(self, item):
        return item in self.__arr

    def updated(self, item):
        """
        A function that moves an updated element up or down the heap,
        as appropriate, to satisfy the heap property.
        :param item: The updated object
        :return: The new index of the element, if successful
        """
        def intkey(ind):
            return self.key(self.__arr[ind])

        i = self.__arr.index(item)
        if intkey(i) < intkey(Heap.parent(i)):
            return Heap._move_up(i, self.__arr, key=self.key)
        elif [c for c in Heap.children(i, len(self.__arr)) if intkey(c) < intkey(i)]:
            return Heap._sift(i, self.__arr, key=self.key)

    @staticmethod
    def heapify(arr, key=lambda arg: arg):
        """Modifies the array in place, making it satisfy the heap property"""

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
    def _move_up(n, arr, key=lambda arg: arg):
        def intkey(i):
            return key(arr[i])
        while Heap.parent(n) >= 0 and intkey(n) < intkey(Heap.parent(n)):
            arr[n], arr[Heap.parent(n)] = arr[Heap.parent(n)], arr[n]
            n = Heap.parent(n)
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
    while h:
        yield h.extract_min()


class PriorityQueue:
    """A queue in which items are sorted by priority.
        Uses an underlying heap representation.
    """

    def __init__(self, arr, key=lambda arg: arg):
        self.__heap = Heap(arr, key=key)

    def get_min(self):
        return self.__heap.get_min()

    def pop(self):
        return self.__heap.extract_min()

    def push(self, x):
        self.__heap.add(x)

    def push_all(self, xs):
        self.__heap.add_all(xs)

    def updated_key(self, item):
        self.__heap.updated(item)

    def __contains__(self, item):
        return item in self.__heap

    def __bool__(self):
        return bool(self.__heap)
