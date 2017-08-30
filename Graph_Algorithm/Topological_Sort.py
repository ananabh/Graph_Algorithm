from queue import Queue


def sort(graph):
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
