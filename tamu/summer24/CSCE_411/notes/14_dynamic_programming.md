# Dynamic Programming
- Similar to divide and conquer, dynamic programming solves problems by combining solutions to subproblems.
> In this context the term **programming** refers mathematical programming, which is a synonym for optimization. It has nothing to do with programming a computer.
- The key difference is that divide and conquer partitions the problem into *disjoint* subproblems.
- Dynamic programming partitions the problem into *overlapping* subproblems, and reuses solutions to subproblems that have already been solved.
- DP (dynamic programming) often applies to optimization problems.
    - These are problems where we want to find the best solution from a set of possible solutions.
    - We call such solution *an* optimal solution opposed to *the* optimal solution, because there may be multiple solutions that are equally good.
- We follow a general recipe to solve DP problems:
    1. Characterize the structure of an optimal solution.
    2. Recursively define the value of an optimal solution.
    3. Compute the value of an optimal solution (typically in a bottom-up fashion).
    4. Construct an optimal solution from computed information.
## Example: Rod Cutting
- Suppose some company has a bunch of steel rods and cuts them into short rods that they sell.
- Each cut is free.
- We want to find the best way to cut the rods to maximize profit.
- We have a table for $i = 1, 2, \ldots, n$ that gives the price $p_i$ for a rod of length $i$.
- The length of a rod is always an integer.
- The **rod-cutting problem** is the following:

Given a rod of length $n$ inches and a table of prices $p_i$ for $i = 1, 2, \ldots, n$, determine the maximum revenue $r_n$ obtainable by cutting up the rod and selling the pieces. If the price $p_n$ for a rod of length $n$ is large enough, an optimal solution may require no cutting at all.

- Suppose we have the following table of prices:
$$\begin{array}{l|cccccccccc}
\text{length } i & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline
\text{price } p_i & 1 & 5 & 8 & 9 & 10 & 17 & 17 & 20 & 24 & 30
\end{array}$$
- Consider a rod of length $n = 4$.
- There are a total of $8$ ways to cut this, or $2^{n-1}$ ways.
- This is because at each inch of rod, we can either cut or not cut, meaning we have two choices for each inch.
- In the case of a rod of length $4$, we have the following ways to cut:
    1. $4$
    2. $1, 3$
    3. $2, 2$
    4. $3, 1$
    5. $1, 1, 2$
    6. $1, 2, 1$
    7. $2, 1, 1$
    8. $1, 1, 1, 1$
- The optimal solution is to cut the rod into two pieces of length $2$ each, which gives us a revenue of $5 + 5 = 10$.
- Generally, the optimal decomposition of the rod $n = i_1 + i_2 + \ldots + i_k$ for some $1 \leq k \leq n$ is the one that maximizes the revenue $r_n = p_{i_1} + p_{i_2} + \ldots + p_{i_k}$.
- Thus, we can express the values of $r_n$ for $n \geq 1$ in terms of optimal revenues from shorter rods.
$$ r_n = \max(p_n, r_1 + r_{n-1}, r_2 + r_{n-2}, \ldots, r_{n-1} + r_1) $$
- Here, $p_n$ is the revenue from selling a rod of length $n$ as is.
- The rest of the $n-1$ terms represent the revenue from first cutting the rod into two pieces of length $i$ and $n-i$, and then optimally cutting those two pieces.
- We say that the rod-cutting problem exhibits *optimal substructure*: an optimal solution to the problem contains within it optimal solutions to subproblems.
- The expression for $r_n$ can be further simplified as:
$$ r_n = \max \{p_i + r_{n-i} : 1 \leq i \leq n\} $$
- Here, an optimal solution uses only one related subproblem, not two.
### Recursive Top-Down Implementation
- A simple recursive top-down implementation of the rod-cutting problem is as follows:
```pseudo
cut_rod(p, n)
    if n == 0
        return 0
    q = -∞
    for i = 1 to n
        q = max(q, p[i] + cut_rod(p, n-i))
    return q
```
- This algorithm has an exponential time complexity of $O(2^n)$.
- This is because the algorithm solves the same subproblems multiple times.
- Here we are not using dynamic programming, since we are not storing and reusing solutions to subproblems.
### A dynamic programming approach
- Instead of solving the same subproblems multiple times in the naive recursive approach, we can store the solutions to subproblems in a table and reuse them.
- If we need to reuse a solution, we can simply look it up in the table.
- Saving solutions comes with a cost of additional memory, but it can save a lot of time.
- This is an example of a **time-memory tradeoff**.
- The time savings, however, can be dramatic.
- In the case of the rod cutting problem, we can solve it in $\Theta(n^2)$ time.
- Typically there are two ways to implement dynamic programming:
    1. **Top-down with memoization**
        - This is similar to the natural recursive formulation, except we store the solutions to subproblems in a table (usually an array or hash table).
        - The procedure checks if the subproblem has already been solved, and if so, it returns the solution from the table.
        - We say this procedure has been **memoized**: it remembers the previous solutions.
    2. **Bottom-up method**
        - This approach typically depends on some natural notion of the "size" of a subproblem.
        - We try to solve the smallest subproblems first, and then use their solutions to solve larger subproblems.
        - This way, we already have our prior solutions before we need them.
- The two approaches have the same asymptotic running time, except when the top-down approach does not actually examine all possible subproblems.
- The bottom up approach typically has better constant factors.
- The following is a bottom-up implementation of the rod-cutting problem:
```pseudo
let r[0:n] be a new array
r[0] = 0
for j = 1 to n
    q = -∞
    for i = 1 to j
        q = max(q, p[i] + r[j-i])
    r[j] = q
return r[n]
```
### Subproblem Graphs
- We can visualize the subproblems of a dynamic programming problem as a graph.
- This is the **subproblem graph** for the rod-cutting problem of length $n = 4$:
```tikz
\begin{document}
\begin{tikzpicture}[
    node distance = 1cm and 2cm,
    every node/.style = {circle, draw, minimum size=1cm}
]

\node (4) at (0,8) {4};
\node (3) at (0,6) {3};
\node (2) at (0,4) {2};
\node (1) at (0,2) {1};
\node (0) at (0,0) {0};

\draw[->] (4) to (3);
\draw[->] (4) to[bend right=40] (2);
\draw[->] (4) to[bend right=60] (1);
\draw[->] (4) to[bend right=80] (0);

\draw[->] (3) to (2);
\draw[->] (3) to[bend left=40] (1);
\draw[->] (3) to[bend left=60] (0);

\draw[->] (2) to (1);
\draw[->] (2) to[bend right=40] (0);

\draw[->] (1) to (0);

\end{tikzpicture}
\end{document}
```
- A subproblem graph is a directed graph with one vertex for each distinct subproblem.
- There exists a directed edge from subproblem $x$ to subproblem $y$ if detmining an optimal solution for $x$ involves solving subproblem $y$.
- This is kind of like a collapsed version of the recursion tree.
- The size of the subproblem graph $G = (V, E)$ can help you determine the time complexity of the dynamic programming algorithm.
- Typically, the time to compute the solution to a subproblem is proportional to the number of outgoing edges from that subproblem.
## Example: Matrix-Chain Multiplication
## Elements of Dynamic Programming
- There are two things a problem must have for dynamic programming to apply.
### Optimal Substructure
- The first step in solving an optimization problem with dynamic programming is to characterize the structure of an optimal solution.
- A problem has **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.
- This is necessary for dynamic programming to work.
- There is a common pattern in discovering optimal substructure:
    1. A solution to the problem consists of making a choice, and making that choice leaves one or more subproblems to solve.
    2. You suppose that for a given problem, you are given the choice that leads to an optimal solution.
    3. You then determine which subproblems arise from making that choice.
    4. You then determine the structure of an optimal solution to the problem by deriving contradictions and only considering the choice that leads to an optimal solution.
- A good rule of thumb is to try to keep the subproblem space as small as possible and expand as needed.
- Optimal substructure varies across problems in two ways:
    1. How many subproblems an optimal solution to the original problem uses.
    2. How many choices we have in determining an optimal solution.
### Overlapping Subproblems