from GraphRepresentation.GraphNode import GraphNode


class CorruptedInputException(Exception):
    """This exception is raised when the input for the graph is incorrect."""


class Graph:
    """The base class to hold a graph.
        The graph is represented by a list of GraphNode objects and a list of edges.
        The edges are tuples of type ((source, destination), cost)
        Supported operations:
            - reading from file
            TODO: adding a node
                  adding an edge
    """

    def __init__(self, source='graphtxt.txt', weighted=True, directed=True):
        self.nodes = []
        self.edges = []
        self.numOfNodes = 0
        self.numOfEdges = 0
        self.weighted = weighted
        self.directed = directed

        extension = source.split('.')[-1]

        if extension in ['txt', 'in']:
            self.__read_from_file(source)
        elif extension == 'csv':
            raise NotImplementedError('CSV reading not yet implemented.')
        else:
            raise CorruptedInputException('Unrecognised file format!')

    def __read_from_file(self, filename):
        """This function reads a graph from a file.
            The file should be formatted as follows:
            - the first line should be the number of nodes, n
            - the second line should be the number of edges, m
            - all the subsequent m lines should contain one edge on each,
                in the format:
                source, destination(, cost if weighted)
            This will generate a graph with n nodes, and add each edge both to the
            neighbours list of the source (and dest), as well as to the list of all edges.
        """

        file = open(filename)
        line = file.readline()
        self.numOfNodes = int(line.strip())

        # create all the new nodes
        for i in range(self.numOfNodes):
            self.nodes.append(GraphNode())

        line = file.readline()
        self.numOfEdges = int(line.strip())

        if self.weighted: linelength = 3
        else: linelength = 2

        for line in file:
            att = line.split(',')

            if len(att) != linelength:
                raise CorruptedInputException("Number of items on a line must be "
                                              + str(linelength)
                                              + " not "
                                              + str(len(att)))

            source_node = self.nodes[int(att[0].strip())]
            dest_node = self.nodes[int(att[1].strip())]
            if self.weighted:
                cost = int(att[2].strip())
            else:
                cost = 1

            self.edges.append(((source_node, dest_node), cost))
            source_node.neighbours.append((dest_node, cost))
            if not self.directed:
                dest_node.neighbours.append((source_node, cost))

        file.close()
        if len(self.edges) != self.numOfEdges:
            raise CorruptedInputException("Declared and true number of edges differ: "
                                          + str(self.numOfEdges)
                                          + " "
                                          + str(len(self.edges)))

    def __read_csv(self):
        pass
        # TODO: make this

    def add_node(self, content=None):
        self.numOfNodes += 1
        self.nodes.append(GraphNode(content=content))

    def add_edge(self, u, v, cost):
        self.numOfEdges += 1
        if not self.weighted:
            cost = 1

        self.edges.append(((u, v), cost))
        u.neighbours.append((v, cost))
        if not self.directed:
            v.neighbours.append((u, cost))

    def __str__(self):
        adj = [[0 for x in range(self.numOfNodes)] for y in range(self.numOfNodes)]
        for ((u, v), c) in self.edges:
            adj[u.id][v.id] = c
            if not self.directed:
                adj[v.id][u.id] = c

        s = ""
        for row in adj:
            for c in row:
                s += "{:3}".format(str(c))
            s += "\n"

        return s
