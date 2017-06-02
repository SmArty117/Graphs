from functools import total_ordering
from typing import Sequence


@total_ordering
class BinomialNode:
    """A node in a binomial tree. It holds a value and a key."""

    def __init__(self, content, key=lambda x: x):
        self.content = content
        self.parent = None
        self.children = []
        self.key = key

    @property
    def nrnodes(self):
        return  2**len(self.children)

    @property
    def degree(self):
        return len(self.children)

    def __eq__(self, other):
        return self.key(self.content) == self.key(other.content)

    def __le__(self, other):
        return self.key(self.content) <= self.key(other.content)

    def __lt__(self, other):
        return self.key(self.content) < self.key(other.content)


class BinomialTree:
    """ A binomial tree, an element of a binomial heap.
        It holds a root, to which a number of 2^degree nodes are
        attached as ancestors.
    """
    def __init__(self, root:BinomialNode):
        self.root = root

    @property
    def degree(self):
        return self.root.degree

    @staticmethod
    def merge(t1, t2):
        if t1.degree != t2.degree:
            raise ValueError('Binomial trees of different degrees cannot be merged!')
        if t1.root <= t2.root:
            t2.root.parent = t1.root
            t1.root.children.append(t2.root)
            return t1
        else:
            t1.root.parent = t2.root
            t2.root.children.append(t1.root)
            return t2

    @property
    def children(self):
        return self.root.children

    # @staticmethod
    # def _local_add(*args):
    #     if len(args) > 3:
    #         raise ValueError('WTF addition?')
    #
    #     if len(args) == 2:
    #         result = BinomialTree.merge(args[0], args[1])
    #         args


class BinomialHeap:

    def __init__(self, iterable, key=lambda x: x):
        self.trees = []
        self.key = key
        for item in iterable:
            self.push(item)

    def push(self, item:BinomialNode):
        temptree = BinomialTree(item)
        self.__add_heap([temptree])

    def pop(self):
        imin, mintree = 0, self.trees[0]
        for (i, tree) in enumerate(self.trees[1:]):
            if tree.root < mintree.root:
                imin, mintree = i, tree
        minval = mintree.root.content

        self.trees[imin] = None
        self.__add_heap(mintree.children)

        return minval

    def get_min(self):
        imin, mintree = 0, self.trees[0]
        for (i, tree) in enumerate(self.trees[1:]):
            if tree.root < mintree.root:
                imin, mintree = i, tree
        return mintree.root.content

    def merge(self, other):
        self.__add_heap(other.trees)

    def updated_key(self, node:BinomialNode):
        while node.parent is not None and node < node.parent:
            p = node.parent
            g = p.parent
            if g is not None:
                g.children.remove(p)
                g.children.append(node)
            p.children.remove(node)
            p.children, node.children = node.children, p.children
            node.children.append(p)
        raise NotImplementedError('Updating keys not supported yet')

    def __add_heap(self, l):
        """ Binary addition motherfucker
            ...Here be dragons
        """
        i = 0
        carry = None
        while i <= max(len(l), len(self.trees)):
            tba = []
            if i < len(self.trees) and self.trees[i] is not None:
                tba.append(self.trees[i])
            if i < len(l) and l[i] is not None:
                tba.append(l[i])
            if carry is not None:
                tba.append(carry)

            if len(tba) == 0:
                pass
            elif len(tba) == 1:
                if i >= len(self.trees):
                    self.trees.append(tba[0])
                else:
                    self.trees[i] = tba[0]
            elif len(tba) == 2:
                carry = BinomialTree.merge(tba[0], tba[1])
                if i >= len(self.trees):
                    self.trees.append(None)
                else:
                    self.trees[i] = None
            elif len(tba) == 3:
                aux = BinomialTree.merge(tba[0], tba[1])
                if i >= len(self.trees):
                    self.trees.append(tba[2])
                else:
                    self.trees[i] = tba[2]
                carry = aux

            i += 1
