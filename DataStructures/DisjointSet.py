class DisjointSet:
    """ A collection of disjoint sets on a universe of elements
        Uses a forest representation.
    """
    def __init__(self, iterable):
        self.roots = []
        self.parent = dict()
        self.rank = dict()
        for x in iterable:
            self.add_singleton(x)

    def add_singleton(self, item):
        self.roots.append(item)
        self.rank[item] = 0
        self.parent[item] = None

    def merge(self, u, v):
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[v] > self.rank[u]:
            self.parent[u] = v
        else:
            self.parent[v] = u
            self.rank[u] += 1

    def find_set(self, item):
        passed = []
        while self.parent[item]:
            passed.append(item)
            item = self.parent[item]
        root = item
        for item in passed:
            self.parent[item] = root
        return root
