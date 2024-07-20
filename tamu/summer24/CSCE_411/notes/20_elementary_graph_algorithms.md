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
- Adjacency lists can also represent **weighted graphs**.
- A weighted graph is a graph in which each edge has an associated **weight** given by a **weight function** $w: E \to \mathbb{R}$.
- If $G$ is a directed graph, the sum of the lengths of all the adjacency lists is $|E|$.
- For directed graphs, the sum of all the adjacency lists is $2|E|$ (since each edge appears on two adjacency lists).
- Adjacency lists require $\Theta(V + E)$ space, and finding each edge also takes $\Theta(V + E)$ time.
- A potential disadvantage of adjacency lists is that there's no quicker way to determine whether a given edge $(u, v)$ is in the graph than to search for $v$ in the adjacency list $Adj[u]$.
- Adjacency matrices solve this issue at a cost of much more memory.
    - The **adjacency-matrix representation** of a graph $G = (V, E)$ assumes the vertices are numbered $1, 2, \ldots, |V|$ in some arbitrary manner.
    - The adjacency matrix is a $|V| \times |V|$ matrix $A = (a_{ij})$ such that $a_{ij} = 1$ if $(i, j) \in E$ or $0$ otherwise.
- Adjacency matrices require $\Theta(V^2)$ space, which is independent of the number of edges in the graph.
- Adjacency matrices are symmetric for undirected graphs and, i.e. $A = A^T$.
- For edges that do not exist, its common to store some nil value, $0$, or $\infty$ depending on the context.
### Representing attributes
- Most algorithms that operate on graphs need to maintain attributes for vertices and/or edges.
- We can denote an attribute $d$ for a vertex $v$ as $v.d$.
- Likewise, we can denote an attribute $f$ for an edge $(u, v)$ as $(u, v).f$.
- Implementing vertex and edge attributes in real programming languages will depend on the situation.
## Breadth-first search
- **Breadth-first search** is one of the simplest algorithms for searching a graph.
    - This is a common archetype for many graph algorithms.
    - Prim's MST algorithm and Dijkstra's shortest path algorithm are based on BFS.
- Given a graph $G = (V, E)$ and a distinguished **source** vertex $s$, BFS will systematically explore the edges of $G$ to discover every vertex that is reachable from $s$.
- BFS computes the distance (smallest number of edges) from $s$ to each reachable vertex.
- Thus, BFS also produces a "breadth-first tree" with root $s$ that contains all reachable vertices.
- BFS works on both directed and undirected graphs.
- BFS is called "breadth-first" because it expands the frontier between discovered and undiscovered vertices uniformly across the breadth of the frontier.
    - One can think of this as discovering verticies in "waves" starting from the source.
    - I.e. BFS discovers all neighbors of $s$, then all neighbors of those neighbors, and so on until all reachable vertices are discovered.
- BFS uses a **first-in, first-out (FIFO)** queue to manage the "waves" of vertices to discover.
- To keep track of progress, BFS colors each vertex white, gray, or black.
    - All vertices are initially white.
    - A vertex is gray while it is in the queue.
    - A vertex is black once it is dequeued.
- Pseudocode for BFS:
```pseudo
BFS(G, s)
    for each vertex u in G.V - {s}
        u.color = WHITE
        u.d = INFINITY
        u.pi = NIL
    s.color = GRAY
    s.d = 0
    s.pi = NIL
    Q = {}
    Q.enqueue(s)
    while Q != {}
        u = Q.dequeue()
        for each v in G.Adj[u]
            if v.color == WHITE
                v.color = GRAY
                v.d = u.d + 1
                v.pi = u
                Q.enqueue(v)
        u.color = BLACK
```
- Here, we assume:
    - The graph $G=(V, E)$ is represented using adjacency lists.
    - Each vertex $u \in V$ has attributes $u.color$, $u.d$, and $u.pi$.
        - $u.color$ is the color of $u$.
        - $u.d$ is the distance from the source $s$ to $u$.
        - $u.pi$ is the predecessor of $u$ in the breadth-first tree.
- BFS works as follows:
    - We initialize all vertices to white, set their distances to $\infty$, and set their predecessors to nil.
    - Then we set the source vertex $s$ to gray, its distance to $0$, and its predecessor to nil.
    - Initialize an empty queue $Q$ and enqueue the source vertex $s$.
    - While the queue is not empty:
        - Dequeue a vertex $u$.
        - For each vertex $v$ adjacent to $u$:
            - If $v$ is white, set $v$ to gray, set its distance to $u$'s distance plus $1$, set its predecessor to $u$, and enqueue $v$.
        - Set $u$ to black.
### Analysis
- After initialization, BFS will never whiten (we cannot undiscover) a vertex.
- Enqueuing and dequeuing a vertex takes $O(1)$ time.
- Thus, the queue operations are in $O(V)$.
- We scan the entire adjacency list of each vertex
    - The length of *all* of the adjacency lists is $\Theta(E)$.
    - Thus the total time spent scanning adjacency lists is $O(V + E)$.
- The total running time of BFS is $O(V + E)$.
- BFS runs in time linear in the size of the adjacency list representation of the graph.
### Shortest paths
- BFS will compute the shortest path from the source vertex $s$ to every other vertex $v$.
- Define the **shortest-path distance** $\delta(s, v)$ from $s$ to $v$ as the minimum number of edges in any path from $s$ to $v$.
    - If there is no path from $s$ to $v$, then $\delta(s, v) = \infty$.
    - Otherwise, we call a path of length $\delta(s, v)$ a **shortest path** from $s$ to $v$.
## Depth-first search
- DFS searches "deeper" in the graph whenever possible.
    - First explore the edges out of the most recently discovered vertex $v$ that still has unexplored edges leaving it.
    - Once all of $v$'s edges have been explored, DFS "backtracks" to explore edges leaving the vertex from which $v$ was discovered.
    - Repeat this process until all vertices are discovered.
- Unlike BFS, DFS does not produce a breadth-first tree.
    - Instead, DFS produces a predecessor subgraph.
    - This might contain multiple trees 
## Topological sort
## Strongly connected components