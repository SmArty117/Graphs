class FibonacciHeapNode:
    """An element of a fib-heap"""

    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        self.parent = None
        self.child = None
        self.degree = None
        self.flag = False

    def reset(self):
        self.left = None
        self.right = None
        self.parent = None
        self.flag = False
        return self

    def traverse(self):
        yield self
        current = self.right
        while current is not self:
            yield current
            current = current.right


class FibonacciHeap:
    """A type of priority queue that is lazy"""

    def __init__(self, iterable, key=lambda arg: arg):
        self.min = None
        self.cont_key = key
        for item in iterable:
            self.push(FibonacciHeapNode(item))

    def key(self, node:FibonacciHeapNode):
        return self.cont_key(node.content)

    def push(self, node:FibonacciHeapNode):
        if self.min is None:
            self.min = node.reset()
            self.min.right = self.min
            self.min.left = self.min
        else:
            node.reset()
            node.right = self.min.right
            self.min.right.left = node
            node.left = self.min
            self.min.right = node
            if self.key(node) < self.key(self.min):
                self.min = node

    def merge(self, f):
        """ UNTESTED AND POTENTIALLY DANGEROUS """
        oldleft = self.min.left
        self.min.left = f.min.left
        self.min.left.right = self.min
        f.min.left = oldleft
        oldleft.right = f.min

        if self.key(f.min) < self.key(self.min):
            self.min = f.min
        return self

    def get_min(self):
        return self.min.content

    def __cut(self, node:FibonacciHeapNode):
        continuing = True
        while continuing:
            if node.parent is None:
                continuing = False
            else:
                if node.parent.child is node:
                    if node.right is not node:
                        node.parent.child = node.right
                    else:
                        node.parent.child = None

                if not node.parent.flag:
                    node.parent.flag = True
                    continuing = False

                node.left.right = node.right
                node.right.left = node.left
                node.parent.degree -= 1

                parent = node.parent
                self.push(node)
                node = parent

    def __link(self):
        raise NotImplementedError('Linking step not implemented yet.')

    def pop(self):
        # cut all the children of min
        while self.min.child:
            self.__cut(self.min.child)

        # cut min out
        contmin = self.min.content
        self.min.right.left = self.min.left
        self.min.left.right = self.min.right
        self.min = self.min.right

        # perform the linking step
        self.__link()

        # find new minimum root
        node = self.min.right
        running_min = self.min
        while node is not self.min:
            if self.key(node) < self.key(running_min):
                running_min = node
            node = node.right
        self.min = running_min

        return contmin
