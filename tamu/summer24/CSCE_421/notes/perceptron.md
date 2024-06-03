# Perceptron
## Biological Inspiration
- The **Perceptron** is a simple model of a neuron, mimicking the way a biological neuron works
- Biological neurons:
    - Connected to other neurons through synapses
    - Axons carry signals from the neuron to the synapse
    - Information is only sent between neurons if the signal is strong enough to pass a certain threshold
    - Synapses are modified with learning
- The perceptron was the first algorithmically described neural network
- Mathematically, the perceptron models a neuron as follows:
    - The neuron receives input signals $x_1, x_2, \ldots, x_n$
    - Each input signal is multiplied by a weight $w_1, w_2, \ldots, w_n$
    - The weighted sum of the inputs is calculated: $\sum_{i=1}^{n} w_i x_i = w^T x$
    - The weighted sum is passed through an activation function $f(z)$
    - The output of the neuron is $y = f(z)$
- The weights can be thought of synaptic weights
- The activation function is the threshold to determine if the neuron fires
## Overview
- The perceptron produces continuous output, however it can be easily converted for classification
- The perceptron can be treated as a binary classifier
- However, the perceptron is limited to linearly separable data in the case of binary classification
- With only one neuron, the perceptron can only classify between two classes
- Expanding the output layer to have more than one neuron allows for multi-class classification, still limited to linearly separable data
## Linear Separability
- A set of points is **linearly separable** if there exists a hyperplane that separates the points into two classes
- A linearly separable set of points can be classified by a single layer perceptron
- If a set of points is not linearly separable, a multi-layer perceptron can be used
- Formal definition: A dataset $D$ is said to be linearly separable if there exists some unit oracle vector $\mathbf{u} : ||\mathbf{u}|| = 1$ which correctly classifies every example $(\mathbf{x}, t) \in D$ with a margin of at least $\delta > 0$
## Perceptron Architecture
- Has the following:
    - An input vector $x = [x_1, x_2, \ldots, x_n]$
    - A weight vector $w = [w_1, w_2, \ldots, w_n]$
    - A bias term $b$
    - An activation function $f(z)$
    - An output $y = f(w^T x + b)$
- We call the term $w^T x + b$ the **net**, often denoted as $z$
## Activation Functions
- The **rectified linear unit (ReLU)** is a very common activation function
- The ReLU is defined as:
    - $\text{ReLU}(z) = \max(0, z)$
- Additional activation functions include:
    - **Step function** - $y = \begin{cases} 1 & z > 0 \\ 0 & z \leq 0 \end{cases}$
    - **Logistic sigmoid** - $y = \frac{1}{1 + e^{-z}}$
    - **Hyperbolic tangent** - $y = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$
    - **Soft ReLU** - $y = \log 1 + e^z$
- The **sigmoid** is the most common activation function: $y = \frac{1}{1 + e^{-net}}$
> Non-linear activation functions produce non-linear decision boundaries
- Linear activation function: $y = z$
## How the perceptron works
- Suppose we have a perceptron with input $x = [x_1, x_2]$, weights $w = [w_1, w_2]$, and bias $b$
- The output of the perceptron is $y = f(w^T x + b)$
    - This can be expanded to $y = f(w_1 x_1 + w_2 x_2 + b)$
    - The weights and bias are the **learnable parameters** of the perceptron
    - This means that the weights and bias are adjusted during training
- The decision boundary of the perceptron is the line where $w^T x + b = 0$, i.e., the net is set to 0
    - $\text{net} = w_1 x_1 + w_2 x_2 + b = 0$
    - Can be rewritten as $x_2 = -\frac{w_1}{w_2} x_1 - \frac{b}{w_2}$
- Start with random weights and bias
    - Set $x_0 = 0$ to find the $x_1$ intercept
    - Set $x_1 = 0$ to find the $x_2$ intercept
    - Plot the line connecting the two intercepts
- The resulting line is the decision boundary of the perceptron
- One side will be class 1, the other side will be class 0 (-1)
- To find which side of the boundary corresponds to which class, we can just plug in a point
## Another example: Learning the AND gate
- Dataset has the form of $D = \{(x^1, t^1), (x^2, t^2), \ldots, (x^m, t^m)\}$ where $x^i$ is the input and $t^i$ is the target
- In this case we have the dataset $D = \{([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)\}$
- We need to find a line that separates $[0, 0], [0, 1], [1, 0]$ from $[1, 1]$
- Technically, an infinite number of lines can separate the points
- We want to find the halfway point between the two classes
- Now we choose a weight vector $w = [w_1, w_2]$
> The weight vector is **orthogonal** to the decision boundary and can be *any* length
> Recall how a plane in $\mathbb{R}^3$ is defined by a normal vector. The weight vector is the normal vector to the decision boundary.
- Suppose we choose $w = [3, 3]$
- The bias term determines the distance of the decision boundary from the origin
    - To find the bias, start with picking a point on the decision boundary
    - Plug it in for the input vector
    - Use our weight vector and set the net to 0
    - Solve for the bias
- Now test the network with our dataset
- For each input, calculate the output and compare it to the target
- However, finding our weights and bias is not always so simple
- In the real world, weights and biases are found through learning
## System parameters
- Start with our initial weights
- For each training sample $x^i$, calculate $w^T x^i$
- Determine the output with one of these functions:
    - $y = f(x) = \begin{cases} 1 & w^T x \geq 0 \\ 0 & \text{otherwise} \end{cases}$
    - $y = f(x) = \begin{cases} 1 & w^T x \geq 0 \\ -1 & \text{otherwise} \end{cases}$
    - Check if the sample is misclassified by the current weights / decision boundary
- If the classification is correct: $y = d = t$
    - $y$ is the output of the perceptron
    - $d$ is the desired output
    - $t$ is the target
    - No weight update is needed
> Correct classification means that $x$ is on the correct side of the hyperplane defined by $w, t, y \in \{-1, 1\}$
- If the classification is incorrect: $y \neq t$
    - Update the weights: $w \leftarrow w + \Delta w$
    - Adjust the weight vector by adding or subtracting the input (aka feature) vector
    - Subtract if $t$ is $-1$, add if $t$ is $1$
    - Thus, $w = w + t.x$
- If a feature vector is still misclassified, the weight vector will be adjusted again
    - We will make $k$ updates
    - This means we add $t.x$ to the weight vector $k$ times
    - $w = ((w + t.x) + t.x) + t.x + \ldots + t.x$
    - Given linearly separable data, the perceptron will eventually converge

$$
\begin{align}
    &(w + kt.x)^T x \leq 0 \\
    & w^T x + kt.x^T x \leq 0 \\
    & k \leq -\frac{w^T x}{t.x^T x}
\end{align}
$$

## Perceptron Learning Rule
- The **Perceptron Learning Rule** is a simple algorithm for learning the weights of a perceptron
- We have a basic algorithm as follows:
```
w = 0 (or random)                   : initialize weight vector

while TRUE do
    m = 0                           : number of misclassified samples
    for (x^i, t^i) in D             : for each training sample
        if t^i * w^T x^i <= 0       : if misclassified
            w <- w + tx^i           : update weights
            m <- m + 1              : increment misclassified counter
        end if
    end for
    if m == 0                       : if no misclassified samples
        break                       : exit loop
    end if
end while
```
- This only adjusts weights, we can make a more general algorithm that learns the features and minimizes the error
- Error is defined as the difference between the target and the output, $e = t - y$
- Our new algorithm can adjust weights and bias:
    - $w^{\text{new}} = w^{\text{old}} + e x$
    - $b^{\text{new}} = b^{\text{old}} + e$
    - Initial values $w^0$ and $b^0$ are chosen randomly or set to 0
- The perceptron learning rule is as follows:
```
for iteration = 1 to max_iterations do
    for all (x, t)
        y = f(w^T x + b)
        e = t - y
        w(k+1) = w(k) + n*e*x
        b(k+1) = b(k) + n*e
    end for
end for
```
- In the pseudocode above, n (supposed to be $\eta$) is the learning rate
- Learning rate is a hyperparameter that determines how much the weights are adjusted
## Loss Function
- Training actually means finding weights that minimize some loss function
- The loss function for the perceptron is $\mathcal{L}(x, y, w) = \text{max}(0, -t(w^T x + b))$
    - This is zero when the sample is classified correctly
    - When the sample is misclassified, the loss is proportional to the distance from the decision boundary
- Perceptron loss is a special case of the **hinge loss**
### Error functions
- We have several terms for functions that describe the error of a model
    - A **loss function** is defined on a data point, prediction, and label, and measures the penalty for an incorrect prediction
    - A **cost function** is typically more general. It could be a sum of loss functions over the training set plus some regularization term
    - An **objective function** is the most general term for any function that is to be optimized
- Some common cost functions are:
    - **Mean absolute error (MAE)**
    - **Mean squared error (MSE)**
    - **Root mean squared error (RMSE)**
    - **Binary cross-entropy**
    - **Hinge loss**
    - **Categorical cross-entropy**
    - **Sparse categorical cross-entropy**
    - and more
## Gradient notation
- We can rewrite the weight update rule as:
    - $w(k+1) = w(k) + \eta e x$
    - $w(k+1) = w(k) - \eta \nabla \mathcal{L}(w(k))$
        - $\frac{\partial \mathcal{L}}{\partial w_i} = 0$ when $zt > 0$ (no update needed)
        - $\frac{\partial \mathcal{L}}{\partial w_i} = -x_i$ when $t = 1$ and $z < 0$
        - $\frac{\partial \mathcal{L}}{\partial w_i} = x_i$ when $t = -1$ and $z > 0$
## Multiclass decision rule
- The perceptron defines one decision boundary per neuron, defined by $w^T x + b = 0$
- A single neuron perceptron can only classify between two classes
- There can be a total of $2^s$ categories for a perceptron with $s$ neurons
## Hyperparameters
- **Batch size** is the number of samples used in each iteration
    - At the end of each batch, the outputs are calculated and compared to the desired outputs which gives us the error
    - The weights are updated based on the error
    - The training dataset can be divided into one or more batches
- **Epochs** is the number of complete passes through the training dataset
    - One epoch is one forward pass and one backward pass of all the training samples
    - An epoch can be one or more batches
    - Usually after many epochs, all outputs will match the targets, so the model converges
- **Learning rate** is the step size for adjusting the weights
    - A large learning rate can cause the model to overshoot the minimum
    - A small learning rate can cause the model to take a long time to converge
## Margin
- The **margin** is the distance between the decision boundary and the closest point in the training set
- A higher margin is better since it means less chance of misclassification
- Margin is defined as $\gamma = y \frac{x}{||w||} x$
- The perceptron will stop learning when the classification error is zero, but that doesn't mean the margin is maximized
- The margin perceptron algorithm maximizes the margin, and updates the weights when $y(w^T x + b) \leq \gamma$
- This is out of the scope of this course
## Perceptron convergence theorem
- Suppose we have the weight update rule:
    - $w(k+1) = w(k) + x(k)$ if $w(k)^T x \leq 0$
    - $w(k+1) = w(k) - x(k)$ if $w(k)^T x > 0$
- From the first rule, we have $w(k+1) = w(0) + x(1) + x(2) + \ldots + x(i)$
- If $w(0) = 0$, then $w(k+1) = x(1) + x(2) + \ldots + x(i)$
- Assume the following:
    - Input vectors are from two linearly separable classes
    - The solution weight vector $w^*$ exists
- Multiply both sides by $w^*$ to get $(w^*)^T w(k+1) = (w^*)^T x(1) + (w^*)^T x(2) + \ldots + (w^*)^T x(i)$
- By our weight update rule, the terms on the right side are all positive
- Let $\alpha = \min_{x(j)} (w^*)^T x(j)$ for $j = 1, 2, \ldots, k$
- Then we have $(w^*)^T w(k+1) \geq \alpha k$
- By the Cauchy-Schwarz inequality, we have:
    - $||w*||^2 ||w(k+1)||^2 \geq ((w^*)^T w(k+1))^2$
    - $||w*||^2 ||w(k+1)||^2 \geq (\alpha k)^2$
- Now we have a lower bound for the length of the weight vector: $||w(k+1)||^2 \geq \frac{\alpha^2 k^2}{||w*||^2}$
- To find an upper bound, we can apply the squared L2 norm to both sides of the first weight update rule
    - $||w(k+1)||^2 = ||w(k) + x(k)||^2$
    - $||w(k+1)||^2 = ||w(k)||^2 + 2 x(k)^T w(k) + ||x(k)||^2$
- Since $w(k)^T x(k) \leq 0$, we have $||w(k+1)||^2 \leq ||w(k)||^2 + ||x(k)||^2$
- By induction, we have $||w(k+1)||^2 \leq ||w(1)||^2 + \sum_{j=1}^{k} ||x(j)||^2$ (induction hypothesis is our first weight update rule)
- Then our upper bound becomes:
    - $||w(k+1)||^2 \leq \sum_{j=1}^{k} ||x(j)||^2$
    - Let $\beta = \max_j ||x(j)||^2$
    - Then $||w(k+1)||^2 \leq \beta k$
- Combining our upper and lower bounds, we have:

$$ \frac{\alpha^2 k^2}{||w*||^2} \leq ||w(k+1)||^2 \leq \beta k $$

- Rearranging for $k$, we have:

$$ k \leq \frac{\beta ||w*||^2}{\alpha^2} $$

- This implies that weights will converge in a finite number of steps. $\blacksquare$

## Limitations
- The perceptron is limited to linearly separable data
- Can't solve XOR problems
- Many optimal solutions exist for linearly separable data