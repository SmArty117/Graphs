import queue
import math
import warnings

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
    :return: a tuple of two lists: the first is the number of edges to each node
             and the second is the previous node in the shortest path found
    """

    q = queue.Queue()
    d = [math.inf for i in range(g.numOfNodes)]
    prev = [None for i in range(g.numOfNodes)]
    d[s.id] = 0
    prev[s.id] = s
    q.put(s)

    while not q.empty():
        u = q.get()
        for (v, c) in u.neighbours:
            if d[v.id] == math.inf:
                d[v.id] = d[u.id] + 1
                prev[v.id] = u
                q.put(v)

    return d, prev


def dijkstra(g, s):
    """
    Find the shortest paths from a given source on a graph
    The graph having negative-weight cycles will cause
    the algorithm to raise IncompatibleInputException
    :param g: the graph
    :param s: the source node (the actual object, not the id)
    :return: a tuple of two lists: the first is the distance to each node
             and the second is the previous node in the shortest path found
    """
    q = queue.PriorityQueue()

    d = [math.inf for i in range(g.numOfNodes)]
    prev = [None for i in range(g.numOfNodes)]
    popped = [False for i in range(g.numOfNodes)]

    d[s.id] = 0
    prev[s.id] = s
    q.put((s, d[s.id]))

    while not q.empty():
        u, du = q.get()
        popped[u.id] = True
        for (v, c) in u.neighbours:
            newd = du + c
            if newd < d[v.id]:
                if popped[v.id]:
                    raise IncompatibleInputException('A negative weight cycle was found!')
                else:
                    pass
                # TODO: Priority queue properly done?
                # if v is in q decrease the key
                # if not, put v in the queue

    return d, prev


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
