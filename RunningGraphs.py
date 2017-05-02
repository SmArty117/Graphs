import GraphAlgorithms
from GraphRepresentation import Graph

g = Graph(source="GraphRepresentation/wgraph.txt", weighted=True, directed=True)
print('BFS:')
print(GraphAlgorithms.bfs(g, g.nodes[0]))
print('\n\nDijkstra:')
print(GraphAlgorithms.dijkstra(g, g.nodes[0]))
print('\n\nMST by Kruskal:')
print(GraphAlgorithms.kruskal(g))

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
