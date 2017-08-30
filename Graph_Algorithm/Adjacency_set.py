import abc


class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self,v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self,v1,v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self,v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" %v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set) # sorting is only for convenience no significance


class Adjacency_Set(Graph):
    def __init__(self, numVertices, directed=False):
        super().__init__(numVertices,directed)
        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >=self.numVertices or v2 >=self.numVertices or v1<0 or v2 <0:
            raise ValueError("Vertices %d and %d are out of bounds" %(v1,v2))

        # Only unweighted graph is represented here
        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weight >1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v>=self.numVertices :
            raise ValueError("Cannot access vertex %d" %v)

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self,v):
        if v < 0 or v>=self.numVertices :
            raise ValueError("Cannot access vertex %d" %v)

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree +=1
        return indegree

    def get_edge_weight(self,v1,v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i,"-->",v)
