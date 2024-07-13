# Amortized Analysis
- Suppose you go to a gym with a $60 monthly membership fee, and a $3 fee for each visit.
- Say you go to the gym every day for a month.
- The total cost would be $60 + 3 $\times$ 30 = $150.
- An alternative way to look at this would be that every visit costs $5.
- This way, we are **amortizing** the monthly fee over the 30 visits.
- The same applies for analyzing runtimes of algorithms.
- In an **amortized analysis**, we average the time required for a sequence of operations over all the operations.
- This is useful for algorithms that have a sequence of operations that are not all the same.
- Amortized analysis differs from average-case analysis in that probability is *not* involved.
- An amortized analysis guarantees the *average performance of each operation in the worst case*.
## Aggregate analysis
- In **aggregate analysis**, we show that for all $n$, a sequence of $n$ operations takes $T(n)$ *worst-case* time in total.
- Therefore, in the worst case, the average time per operation is $T(n)/n$.
## The accounting method
- In the **accounting method**, we assign different costs to different operations.
- The assigned cost may be more than, less than, or equal to the actual cost.
- The amount we charge for each operation is called the **amortized cost**.
- When an operations amortized cost exceeds its actual cost, we store the difference as **credit**.
- Credit can help pay for later operations whose amortized cost is less than their actual cost.
- However, we must be careful with 
    - We must show that the total amortized cost of a sequence of operations provides an upper bound on the total actual cost.
    - The upper bound must apply to all sequences of operations.
- Let the actual cost of the $i$th operation be $c_i$ and the amortized cost be $\hat{c}_i$.
- Then the following must hold for all sequences of $n$ operations:
$$\sum_{i=1}^{n} \hat{c}_i \geq \sum_{i=1}^{n} c_i$$
- The total credit stored in the data structure is the difference between the total amortized cost and the total actual cost, i.e.:
$$\sum_{i=1}^{n} \hat{c}_i - \sum_{i=1}^{n} c_i$$
- Thus total credit must be nonnegative at all times.
## The potential method
- The **potential method** has a different view on "prepaid work" than the accounting method.
- Here we see work as "potential energy" that can be used to pay for future operations.
- This potential applies to the data structure as a whole, not individual objects within it.
- The method works as follows:
    - An initial data structure $D_0$ has a sequence of $n$ operations performed on it.
    - For each $i \in \{1, 2, \ldots, n\}$, let $c_i$ be the actual cost of the $i$th operation and $D_i$ be the data structure after applying the $i$th operation to $D_{i-1}$.
    - A **potential function** $\Phi$ maps each data structure $D_i$ to a real number $\Phi(D_i)$, which is the potential of $D_i$.
    - The amortized cost $\hat{c}_i$ of the $i$th operation with respect to $\Phi$ is defined as:
    $$\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$$
- Thus the amortized cost of an operation is the actual cost plus any change in potential due to the operation.
- The total amortized cost of the $n$ operations is then:
$$\begin{align*}
\sum_{i=1}^{n} \hat{c}_i &= \sum_{i=1}^{n} (c_i + \Phi(D_i) - \Phi(D_{i-1})) \\
&= \sum_{i=1}^{n} c_i + \Phi(D_n) - \Phi(D_0)
\end{align*}$$
- The second equation follows sinze the $\Phi(D_i)$ terms telescope.