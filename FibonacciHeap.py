class FibonacciHeapNode:
    """An element of a fib-heap"""

    def __init__(self, content=None):
        self.contents = content
        self.left = None
        self.right = None
        self.parent = None
        self.degree = None
        self.flag = None


class FibonacciHeap:
    """A type of priority queue that is lazy"""

    def __init__(self, arr, key=lambda arg: arg):
        pass
