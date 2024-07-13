# Elementary Graph Algorithms
- Here we cover methods for representing a graph and searching a graph.
- Searching a graph means systematically following the edges of a graph to visit its vertices.
- Graph searching algorithms can discover a lot about the structure of a graph.
    - Many algorithms begin by searching their input graph to learn something about its structure.
    - Graph search algorithms are at the heart of many graph algorithms.
## Representations of graphs
- There are two standard ways to represent a graph $G = (V, E)$:
    - A collection of adjacency lists, one for each vertex in $V$.
    - An adjacency matrix
- Adjacency lists are better for sparse graphs, while adjacency matrices are better for dense graphs.
- A graph is **sparse** when $|E|$ is much less than $|V|^2$.
- A graph is **dense** when $|E|$ is close to $|V|^2$.
- Most algorithms assume a graph is represented by an adjacency list, though some assume an adjacency matrix.
- The **adjacency-list representation** of a graph $G = (V, E)$ consists of an array $Adj$ of $|V|$ lists, one for each vertex in $V$.
    - For each vertex $u \in V$, the adjacency list $Adj[u]$ contains all the vertices $v$ such that there is an edge $(u, v) \in E$.
    - That is, $Adj[u]$ is the list of all vertices adjacent to $u$ in $G$.
- Adjacency lists can also represetn **weighted graphs**.
- A weighted graph is a graph in which each edge has an associated **weight** given by a **weight function** $w: E \to \mathbb{R}$.
- If $G$ is a directed graph, the sum of the lengths of all the adjacency lists is $|E|$.
- For directed graphs, the sum of all the adjacency lists is $2|E|$ (since each edge appears on two adjacency lists).
- Adjacency lists require $\Theta(V + E)$ space, and finding each edge also takes $\Theta(V + E)$ time.
- A potential disadvantage of adjacency lists is that there's no quicker way to determine whether a given edge $(u, v)$ is in the graph than to search for $v$ in the adjacency list $Adj[u]$.
- Adjacency matricies solve this issue at a cost of much more memory.
    - The **adjacency-matrix representation** of a graph $G = (V, E)$ assumes the verticies are numbered $1, 2, \ldots, |V|$ in some arbitrary manner.
    - The adjacency matrix is a $|V| \times |V|$ matrix $A = (a_{ij})$ such that $a_{ij} = 1$ if $(i, j) \in E$ or $0$ otherwise.
- Adjacency matricies require $\Theta(V^2)$ space, which is independent of the number of edges in the graph.
- Adjacency matricies are symmetric for undirected graphs and, i.e. $A = A^T$.
- For edges that do not exist, its common to store some nil value, $0$, or $\infty$ depending on the context.
### Represnting attributes
- Most algorithms that operate on graphs need to maintain attributes for vertices and/or edges.
- We can denote an attribute $d$ for a vertex $v$ as $v.d$.
- Likewise, we can denote an attribute $f$ for an edge $(u, v)$ as $(u, v).f$.
- Implementing vertex and edge attributes in real programming languages will depend on the situation.
## Breadth-first search
- **Breadth-first search** is one of the simplest algorithms for searching a graph.
    - This is a common archetype for many graph algorithms.
    - Prim's and Dijkstra's algorithms are based on BFS.
## Depth-first search
## Topological sort
## Strongly connected components