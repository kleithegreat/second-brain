# Greedy Algorithms
- Algorithms for optimization typically go through a sequence of steps.
- For many optimization problems, DP may be overkill.
- A **greedy algorithm** is an algorithm that makes the choice that looks best at the moment.
- In other words, a locally optimal choice is made in the hope that this choice will lead to a globally optimal solution.
- Greedy will not always lead to the optimal solution, but it will for many problems.
## An activity-selection problem
## Elements of the greedy strategy
- The greedy heuristic will only work on some optimization problems.
- Here we discuss some general properties of problems for which greedy algorithms work.
- Formulating a greedy algorithm typically consists of the following steps:
    1. Cast the optimization problem as one in which we make a choice and are left with one subproblem to solve.
    2. Prove that there is always an optimal solution to the original problem that makes the greedy choice, so that the greedy choice is always safe.
    3. Demonstrate optimal substructure by showing that, having made the greedy choice, what remains is a subproblem with the property that if we combine an optimal solution to the subproblem with the greedy choice we have made, we arrive at an optimal solution to the original problem.
- Beneath every greedy algorithm, there is always a more cumbersome dynamic programming solution.
- Two key ingredients are the greedy-choice property and optimal substructure.
### Greedy-choice property
- The **greedy-choice property** is that a globally optimal solution can be made by making locally optimal (greedy) choices.
- In other words, you make the choice that looks best in the current problem, without considering results from subproblems.
- The difference between this and dynamic programming is that dynamic programming will make the globally optimal choice by considering results from subproblems.
    - DP typically builds up solutions bottom up, and reuses solutions to subproblems.
    - Greedy can make choices top-down without worrying about subproblems.
- The caveat is that we need to prove that the greedy choice is always safe.
- Greedy choices are typically safer when there are more choices to make.
### Optimal substructure
- As with dynamic programming, a problem exhibits **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.
- This is essential for both DP and greedy algorithms.
- A more direct approach to optimal substructure is common in greedy algorithms, since we only need to make the greedy choice and solve the subproblem.
- This comes from the greedy-choice property (and thus needing to prove it).
- This scheme implicitly uses induction on the subproblems to prove that making the greedy choice at each step leads to an optimal solution.
### Greedy versus dynamic programming
- Since both greedy and DP exploit optimal substructure, you might be tempted to use DP when greedy suffices, or mistakenly use greedy when DP is needed.