from DataStructures.Heap import Heap


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
