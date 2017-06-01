import GraphAlgorithms
from GraphRepresentation import Graph
import copy

g = Graph(source="GraphRepresentation/wgraph.txt", weighted=True, directed=True)

section = '\n\n' + '='*150

print('BFS:')
print(GraphAlgorithms.bfs(g, g.nodes[0]))

print(section)
print('\nDijkstra:')
print(GraphAlgorithms.dijkstra(g, g.nodes[0]))

print('\nBellman-Ford:')
print(GraphAlgorithms.bellman_ford(g, g.nodes[0]))

print(section)
print('\nAll Pairs Shortest Paths, by Johnson:')
john = GraphAlgorithms.johnson(g)
for s in john:
    print(str(s) + ': ' + str(john[s]))

print(section)
print('\nTransitive closure by Floyd-Warshall:')
fw = GraphAlgorithms.floyd_warshall(g)
for (i, l) in enumerate(fw):
    print('From ' + str(i) + ': ' + str(l))

print(section)
gg = copy.copy(g).make_undirected()
print('\nMST by Kruskal:')
print(GraphAlgorithms.kruskal(gg))

print('\nMST by Prim:')
print(GraphAlgorithms.prim(gg))


# a = [3, 5, 2, 7, 0, 10, 4, 11, 12, 1, 25, 16, 12]
# # print(list(Heap.children(3, 10)))     -- tested
# print('\n\n')
# print(a)
# print('heapify:')
# print(Heap.heapify(a))
# print('heapsort:')
# print(list(heapsort(a)))
# print('heapsort on tuples:')
# b = [(x, 100-18*x+x**2) for x in a]
# print(list(heapsort(b, key=lambda t: t[1])))
