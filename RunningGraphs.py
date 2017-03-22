from Graph import Graph
import GraphAlgorithms
from DataStructures import Heap, heapsort

g = Graph(source="graphtxt.txt", weighted=False, directed=True)

print(GraphAlgorithms.bfs(g, g.nodes[0]))

a = [3, 5, 2, 7, 0, 10, 4, 11, 12, 1]
print(list(Heap.children(3, 10)))
Heap.heapify(a)
print(a)
h = Heap(a)
