Graph_Algorithm
==========

Graph_Algorithm is a library for Four main graph algorithms : Graph Search, Topological Sort , Shortest Path , Spanning Tree.

Graphs are excellent tools for modelling complex relationship. Generally we focus on :
  1. Visit all the nodes present within it in order to process them [BFS and DFS]
  2. Establishing precedence relationship between various nodes in a graph [Topological Sort]
  3. Finding shortest or lower cost path from one point to other [Dijkstra's Algorithm]
  4. Covering all nodes in a graph with minimum cost [Minimum Spanning Tree]
	
You should totally check out the Demo for implementation details.

Usage
-----
If you want to use the algorithms in your code it is as simple as:

```python

from Graph_Algorithm import Adjacency_Matrix,Breadth_First,Depth_First
import numpy as np

g=Adjacency_Matrix(9,directed=True)
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

for i in range(9):
	print("Adjacent to :",i,g.get_adjacent_vertices(i))
				
g.display()

Breadth_First.search(g,1) # For BFS
visited = np.zeros(g.numVertices)
Depth_First.search(g,visited,1) # For DFS
```
Contributing:
-------------

Some codes and idea taken from various internet sources. Contributions are always welcome. 
