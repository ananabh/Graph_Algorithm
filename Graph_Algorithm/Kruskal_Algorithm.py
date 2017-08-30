import Graph_Algorithm.priority_dict as priority_dict


def spanning_tree(graph):
    priority_queue=priority_dict.priority_dict()
    for v in range(graph.numVertices):
        for neighbour in graph.get_adjacent_vertices(v):
            priority_queue[(v,neighbour)]=graph.get_edge_weight(v,neighbour)

    visited_vertices=set()
    spanning_tree={}

    for v in range(graph.numVertices):
        spanning_tree[v]=set()

    num_edges=0

    while len(priority_queue.keys())>0 and num_edges < graph.numVertices-1:
        v1,v2 =priority_queue.pop_smallest()
        if v1 in spanning_tree[v2]:
            continue

        vertex_pair=sorted([v1,v2])
        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edges+=1

        visited_vertices.add(v1)
        visited_vertices.add(v2)

    print("Visited Vertices :", visited_vertices)

    if len(visited_vertices) != graph.numVertices:
        print("Minimum spanning tree not found")
    else:
        print("Minimum spanning tree :")
        for key in spanning_tree:
            for value in spanning_tree[key]:
                print(key,"-->",value)


def has_cycle(spanning_tree):
    for source in spanning_tree:
        q=[]
        q.append(source)
        visited_vertices=set()
        while len(q)>0:
            vertex=q.pop(0)

            if vertex in visited_vertices:
                return True

            visited_vertices.add(vertex)
# adding adjacent neighbour to our queue
            q.extend(spanning_tree[vertex])
    return False
