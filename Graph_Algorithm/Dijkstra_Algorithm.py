import Graph_Algorithm.priority_dict as priority_dict


def build_distance_table(graph,source):
    distance_table = {}
    for i in range(graph.numVertices):
        distance_table[i] = (None,None)
    distance_table[source] = (0, source)
    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:
        current_vertex=priority_queue.pop_smallest()
        current_distance=distance_table[current_vertex][0]
        for neighbour in graph.get_adjacent_vertices(current_vertex):
            distance = current_distance + graph.get_edge_weight(current_vertex,neighbour)
            neighbour_distance=distance_table[neighbour][0]

            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour]=(distance,current_vertex)
                priority_queue[neighbour]=distance
    return distance_table


def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)
    path = [destination]
    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
    if previous_vertex is None:
        print("There is no path from %d to %d" % (source, destination))
    else:
        path = [source] + path
        print("Shortest path is : ", path)

