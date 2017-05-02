
class GraphNode:
    """Represents one node in a graph. Used by the Graph class.
        Holds the list of neighbours of this node as a list of tuples
        of type (node, cost)
    """
    numNodes = 0

    def __init__(self, content=None):
        self.id = GraphNode.numNodes
        GraphNode.numNodes += 1
        self.neighbours = []
        self.content = content

    def __str__(self):
        return '<Node ' + str(self.id) + '/>'

    def __repr__(self):
        res = '<Node ' + str(self.id)
        if self.content is not None:
            res += ': ' + str(self.content)
        res += '/>'
        return res

    #
    # def add_neighbour(self, neighbour, cost=1):
    #     self.neighbours.append((neighbour, cost))
    #
    # def add_neighbours(self, newneighbours):
    #     self.neighbours += newneighbours
    #
    # def degree(self):
    #     return len(self.neighbours)
