import queue
import math
import warnings
import DataStructures

# TODO: conclusion is this first needs implementing data structures
#       such as priority queues, disjoint sets, etc.
#       will do that first


class IncompatibleInputException(Exception):
    """An exception raised when a graph which does not meet the
        requirements is passed to a function.
    """


def bfs(g, s):
    """
    Run breadth-first search on a graph, ignoring edge weights (i.e. cost=1)
    :param g: the graph
    :param s: the source node (the actual object, not the id)
    :return: a list of 2-tuples: the first element is the number of edges to each node
             and the second is the previous node in the shortest path found
    """

    q = queue.Queue()
    for v in g.nodes:
        v.d = math.inf
        v.prev = None

    s.d = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        for (v, c) in u.neighbours:
            if v.d == math.inf:
                v.d = u.d + 1
                v.prev = u
                q.put(v)

    return list([(v.d, v.prev) for v in g.nodes])


def dijkstra(g, s):
    """
    Find the shortest paths from a given source on a graph
    The graph having negative-weight cycles will cause
    the algorithm to raise IncompatibleInputException
    :param g: the graph
    :param s: the source node (the actual object, not the id)
    :return: a list of 2-tuples: the first is the distance to each node
             and the second is the previous node in the shortest path found
    """
    q = DataStructures.PriorityQueue([], key=lambda x: x.d)

    for v in g.nodes:
        v.d = math.inf
        v.prev = None
        v.popped = False

    s.d = 0
    q.push(s)

    while q:
        u = q.pop()
        u.popped = True
        for (v, c) in u.neighbours:
            newd = u.d + c
            if newd < v.d:
                if v.popped:
                    raise IncompatibleInputException('A negative weight cycle was found!')
                else:
                    v.d = newd
                    v.prev = u
                    if v in q:
                        q.updated_key(v)
                    else:
                        q.push(v)

    return list([(v.d, v.prev) for v in g.nodes])


def kruskal(g):
    """
    Find a minimum spanning tree of an undirected graph g
    :param g: an undirected graph
    :return: the list of edges in the MST
    """

    if g.directed:
        warnings.warn('The graph should be undirected!')

    sol = []
    es = sorted(g.edges, key=lambda e: e[2])    # sort edges by cost
    # declare a partition of the graph

    for edge in es:
        pass
        # if edge connects nodes in different components,
        # add to sol, unify components

    return sol
