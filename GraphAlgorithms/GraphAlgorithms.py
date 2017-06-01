import queue
import math
import warnings
import copy

import DataStructures
from GraphRepresentation import Graph


class IncompatibleInputException(Exception):
    """An exception raised when a graph which does not meet the
        requirements is passed to a function.
    """


def bfs(g:Graph, s):
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

    return {v: (v.d, v.prev) for v in g.nodes}


def dijkstra(g:Graph, s):
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

    return {v: (v.d, v.prev) for v in g.nodes}


def kruskal(g:Graph):
    """
    Find a minimum spanning tree of an undirected graph g
    :param g: an undirected graph
    :return: the list of edges in the MST
    """

    if g.directed:
        warnings.warn('The graph should be undirected!')

    sol = []
    es = sorted(g.edges, key=lambda e: e[1])    # sort edges by cost
    part = DataStructures.DisjointSet(g.nodes)

    for ((u, v), c) in es:
        if not part.same_set(u, v):
            sol.append(((u, v), c))
            part.merge(u, v)

    return sol


def bellman_ford(g:Graph, s):
    """
    Find the shortest paths to all nodes from a source node s in a graph.
    :param g: A graph
    :param s: The source node
    :return: A dict of type {node: (distance, predecessor)}
    """

    pred = {v: None for v in g.nodes}
    d = {v: math.inf for v in g.nodes}
    d[s] = 0

    for i in range(g.numOfNodes):
        for ((u, v), c) in g.edges:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                pred[v] = u

    for ((u, v), c) in g.edges:
        if d[v] > d[u] + c:
            raise IncompatibleInputException('Negative weight cycle detected!')
        else:
            return {v: (d[v], pred[v]) for v in g.nodes}


def johnson(g: Graph):
    """
    Find the shortest paths between all pairs of nodes in a graph.
    :param g: The given graph.
    :return: A dict of dicts of type {source: {node: (distance, predecessor)}}.
    """
    gg = copy.copy(g)

    # add a supersource to the graph
    s = gg.add_node('S')
    for node in gg.nodes:
        if node is not s:
            gg.add_edge(s, node, 0)

    # run bellman-ford, tweak the graph
    bf = bellman_ford(gg, s)
    d = dict()
    for node in gg.nodes:
        d[node] = bf[node][0]
    for (i, ((u, v), c)) in enumerate(gg.edges):
        gg.edges[i] = ((u, v), d[u] + c - d[v])

    # run Dijkstra from each vertex
    ans = dict()
    for u in gg.nodes:
        if u is not s:
            temp = dijkstra(gg, u)
            ans[gg.isomorph(g, u)] = {gg.isomorph(g, v): (temp[v][0] - d[u] + d[v],
                                                          gg.isomorph(g, temp[v][1]))
                                      for v in temp if v is not s}
    return ans
