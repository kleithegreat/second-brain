# Gradient Descent
- Gradient descent is a method of **optimization**
    - Optimization is the process of finding the maximum or minimum value of some quantity
    - Formally, optimizing some function $f(\theta)$ means finding the value of $\theta^* = \arg\min_\theta f(\theta)$ subject to constraints on $\theta$
    - Maximizing $f(\theta)$ is equivalent to minimizing $-f(\theta)$
- In machine learning, we are interested in learning the parameters of a model
- Therefore, we are interested in minimizing the loss function of the model
- From vector calculus, the minimum of a function $f(\theta)$ must be at a point where $\frac{\partial f}{\partial \theta} = 0$
- Then this equation can be solved analytically to find $\theta$
- In reality, we often emply iterative methods since finding the minimum of a function analytically is often infeasible
## Algorithm
- Given a starting point
- Repeat:
    - Calculate the gradient $\nabla J(\theta)$
    - Update $\theta \leftarrow \theta - \mu \nabla J(\theta)$
- Until **convergence criterion** is satisfied
- Some convergence criteria:
    - Change in objective function is close to zero
    $$ |J(\theta(k+1)) - J(\theta(k))| < \epsilon $$
    - Gradient norm is close to zero
    $$ ||\nabla J(\theta)|| < \epsilon $$
    - Validation error starts increasing (called **early stopping**)
- A global minimum can only be found on a convex function
## Types of Gradient Descent
1. Batch Gradient Descent
2. Stochastic Gradient Descent
3. Mini-batch Gradient Descent
### Stochastic Gradient Descent
- Computes the gradient of the loss function with respect to a single training example per iteration
    - This makes the algorithm much faster and more efficient
    - However, due to randomness, the algorithm may never converge to the global minimum
- Has two variants:
    - Mini-batch SGD: Where gradient descent is done for a random subset of the training data
    - Momentum SGD: Where a momentum term is added to the gradient to prevent the algorithm from getting stuck in local minima
- Used often in deep learning
- The best batch sizes are usually 32, 4, or 2
### Batch Gradient Descent
- Computes the gradient of the loss function with respect to the entire training set
    - Computationally expensive
    - Has the advantage of being more stable and overfit less
- Usuall used in smaller models with small datasets
- E.g. linear regression, logistic regression
### Mini-batch Gradient Descent
- A compromise between batch and stochastic gradient descent
- Computes the gradient of the loss function with respect to a small random subset of the training set
- The mini-batch size is a trade off between speed and stability
- Widely used in deep learning
## Learning Rate
- The learning rate $\mu$ is a hyperparameter that determines the size of the step taken in the direction of the gradient
- This choice of this can impact:
    - Convergence speed
    - Whether the algorithm converges at all
- If the learning rate is too small, the algorithm may take a long time to converge
- Large moves may cause the algorithm to overshoot the minimum every time, never converging
- There are different ways to choose the learning rate
    - The ideal size may be too costly to compute
    - Varies depending on both data and the chosen GD algorithm
- Learning rate scheduling
    - Time based decay: takes the following form
    $$ \mu = \frac{\mu_0}{1 + kt} $$
    - where $\mu_0$ is the initial learning rate, $t$ is a hyperparameter, and $k$ is the iteration number
    - Exponential decay
    $$ \mu = \mu_0 e^{-kt} $$
    - Cosine annealing
        - Begins with a large learning rate and decreases it rapidly to a minimum
        - Then increases it again and repeats the process
        - The idea is that this mimics restarting the leraning process, but better performing weights are maintained
        $$ \mu_t = \mu^i_{min} + \frac{1}{2}(\mu^i_{max} - \mu^i_{min})(1 + \cos(\frac{T_{cur}}{T_i} \pi)) $$
    - Adagrad
        - each parameter has its own learning rate
        - the learning rate is adapted based on the historical gradients
        - Infrequent parameters get a higher learning rate, frequent parameters get a lower learning rate
    - Adadelta
        - An extension of Adagrad that reduces the effects of accumulating historical gradients
        - Instead of accumulating all past gradients, Adadelta has a fixed window of past gradients
    - RMSprop - tries to resolve Adagrad's radically decreasing learning rates
    - Adam (Adaptive Moment Estimation)
        - Uses momentum and scaling
        - Combines methods from SGD and RMSprop
    - Hypergradient descent
        - Optimizes the learning rate itself
        - The learning rate is treated as a parameter and optimized using a second order optimization algorithm