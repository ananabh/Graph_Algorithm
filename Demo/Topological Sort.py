from queue import Queue
from Adjecency_Matrix import *


def topological_sort(graph):
    queue = Queue()
    indegreeMap = {}
    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)
        if indegreeMap[i]==0:
            queue.put(i)

    sortedList = []
    while not queue.empty():
        vertex = queue.get()
        sortedList.append(vertex)
        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] -=1
            if indegreeMap[v] == 0:
                queue.put(v)

    if len(sortedList) != graph.numVertices :
        raise ValueError("This graph has a cycle")

    print(sortedList)


g=AdjacencyMatrixGraph(9,directed=True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)

topological_sort(g)