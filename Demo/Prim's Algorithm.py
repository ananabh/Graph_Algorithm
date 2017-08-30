import priority_dict
from Adjecency_Matrix import *


def spanning_tree(graph,source):
    distance_table={}
    for i in range(graph.numVertices):
        distance_table[i]=(None,None)
    distance_table[source]=(0,source)

    priority_queue=priority_dict.priority_dict()
    priority_queue[source] = 0

    visited_vertices=set()
    spanning_tree =set()

    while len(priority_queue.keys())>0:
        current_vertex=priority_queue.pop_smallest()
        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        if current_vertex != source:
            last_vertex = distance_table[current_vertex][1]
            edge = str(last_vertex) + "--->" + str(current_vertex)
            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            distance=graph.get_edge_weight(current_vertex,neighbour)
            neighbour_distance = distance_table[neighbour][0]

            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour]=(distance,current_vertex)
                priority_queue[neighbour]=distance

    for edge in spanning_tree:
        print(edge)


g = AdjacencyMatrixGraph(8, directed=False)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

spanning_tree(g,1)