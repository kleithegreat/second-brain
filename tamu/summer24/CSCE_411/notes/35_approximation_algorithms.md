# Approximation Algorithms
- Many practical problems are NP-complete, but too important to ignore.
- Even though we can't solve them exactly, we can still find good approximate solutions.
- We have at least three options to get around NP-completeness:
  1. If inputs are small, superpolynomial time may be okay.
  2. There may be special cases of a problem that can be solved in polynomial time.
  3. We can try to find a *near-optimal* solution in polynomial time.
- Practically, near-optimal solutions are often good enough.
- Algorithms that return near-optimal solutions are called **approximation algorithms**.
- In this chapter we study polynomial-time approximation algorithms for NP-complete problems.
## Performance ratios for approximation algorithms
- Say that we have an optimization problem where a potential optimal solution has some positive cost.
- We want to find a near-optimal solution.
- Depending on the problem, the optimal solution may be the maximum or minimum possible cost, i.e. is it a maximization or minimization problem.
- We say an algorithm or problem has an **approximation ratio** of $\rho(n)$ if for any input of size $n$, the cost $C$ of the solution produced by the algorithm is within a factor of $\rho(n)$ of the optimal cost $C^*$.
$$ \max\left(\frac{C}{C^*}, \frac{C^*}{C}\right) \leq \rho(n) $$
- If an algorithm has an approximation ratio of $\rho(n)$, we say it is a **$\rho(n)$-approximation algorithm**.
- These definitions apply for both maximization and minimization problems.
- For maximization problems:
    - $0 < C \leq C^*$
    - The ratio $\frac{C^*}{C}$ is how much costlier the optimal solution is than the approximate solution.
- For minimization problems:
    - $0 < C^* \leq C$
    - The ratio $\frac{C}{C^*}$ is how much costlier the approximate solution is than the optimal solution.
- Since costs are always positive, the approximation ratio is always well-defined and never less than 1.
- Thus, a 1-approxmation algorithm is an exact algorithm producing the optimal solution.
- A large approximation ratio means the solution is much worse than optimal.
- For many problems, we know of good polynomial-time approximation algorithms with small constant approximation ratios.
- However, some problems have approximation ratios that grow with input size.
- One example of this is the set cover problem.
- Some polynomial-time approximation algorithms can achieve better approximation ratios with more computation.
- Thus for such problems, we can trade off approximation ratio for running time.
- One example of this is the subset sum problem.
- An **approximation scheme** for an optimzation problem is an approximation algorithm that takes the input to the problem and a parameter $\epsilon > 0$ such that for any $\epsilon$, the scheme is a $(1 + \epsilon)$-approximation algorithm.
- We say that an approximation scheme is a **polynomial-time approximation scheme** if for any fixed $\epsilon > 0$, the scheme runs in polynomial time.
- However, runtime of polynomial-time approximation schemes may increase rapidly as $\epsilon$ decreases.
- For example, as $\epsilon$ decreases linearly, $O(n^{2/\epsilon})$ increases exponentially.
- We say an approximation scheme is a **fully polynomial-time approximation scheme** if the runtime is polynomial in both the input size and $1/\epsilon$.
- In other words, any constant factor decrease in $\epsilon$ results in a constant factor increase in runtime.
## The vertex-cover problem
- Recall that the *vertex cover* of an undirected graph $G = (V, E)$ is a subset $V' \subseteq V$ such that if $(u, v) \in E$, then $u \in V'$ or $v \in V'$ (or both).
- The size of a vertex cover is the number of vertices in it.
- The *vertex-cover problem* is to find a minimum-size vertex cover, called an **optimal vertex cover**.
- This is the optimization version of the NP-complete decision problem.
- There is no known polynomial-time algorithm for finding an optimal vertex cover.
- However, there is an efficient approximation algorithm that finds a near-optimal solution.
```pseudo
APPROX-VERTEX-COVER(G)
1. C = {}
2. E' = G.E
3. while E' is not empty
4.     let (u, v) be an arbitrary edge of E'
5.     C = C \union {u, v}
6.     remove from E' every edge incident on either u or v
7. return C
```
- The algorithm works as follows:
    1. Initialize an empty set $C$ to store the vertices in the vertex cover.
    2. Initialize a copy $E'$ of the edge set of the graph.
    3. While there are still edges in $E'$:
        1. Choose an arbitrary edge $(u, v)$ from $E'$.
        2. Add both $u$ and $v$ to $C$.
        3. Remove all edges incident on $u$ or $v$ from $E'$.
    4. Return $C$.
- This runs in $O(V + E)$ time.
- The algorithm is a 2-approximation algorithm for the vertex-cover problem.
- The proof is as follows:
    - The set $C$ is a vertex cover because every edge $(u, v)$ has at least one of $u$ or $v$ in $C$.
    - Let $A$ be the set of edges picked in line 4.
    - An optimal cover $C^*$ must contain at least one vertex from each edge in $A$.
    - No two edges in $A$ share a vertex, so we have the lower bound $|C^*| \geq |A|$.
    - In other words, there must be at least one vertex in $C^*$ for each edge in $A$.
    - Since $C$ contains both vertices of each edge in $A$, we have the upper bound $|C| = 2|A|$.
    - Thus, $|C| = 2|A| \leq 2|C^*|$.
    - Therefore, $C$ is a 2-approximation of $C^*$.
    