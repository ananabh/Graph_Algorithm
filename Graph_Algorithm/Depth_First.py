def search(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1
    print("Visit :", current)

    for vertex in graph.get_adjacent_vertices(current):
        search(graph, visited, vertex)
