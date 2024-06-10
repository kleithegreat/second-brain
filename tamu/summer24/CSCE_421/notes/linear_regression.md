# Linear Regression
## Simple Linear Regression
- The simplest form of linear regression is **simple linear regression**
    - This allows us to summarize the relationship between two continuous variables
    - Assume there is only one independent variable $x$ and one dependent variable $y$
    - Then SLR models the relation $y = ax + b$
- For SLR, we aren't interested in deterministic (functional) relationships
    - This is like ohms law, $V = IR$
    - Hookes law, $F = kx$
    - Fahrenheit to Celsius, $C = \frac{5}{9}(F-32)$
- Rather, we are interested in **statistical relationships**
    - This is like the relationship between height and weight
    - The relationship between age and income
    - The relationship between temperature and humidity
- A simple model typically doesn't capture all the variability in the data due to **noise**
- Noise can be:
    - Imprecision in data attributes
    - Errors in data targets (mislabeling)
    - Additional unobserved attributes that affect the target (latent variables)
## Multiple regression
- We can extend SLR to multiple dimensions by adding more independent variables
- Multiple linear regression models the relationship between multiple independent variables and one dependent variable
$$y = a_1x_1 + a_2x_2 + ... + a_nx_n + b$$
- For example, suppose a company wants to predict how much a new employee should be paid
    - They would want to take into consideration many factors like experience, education, certifications, etc.
    - Thus a multiple regression model would be appropriate
### Polynomial regression
- Another extension of SLR is polynomial regression
- Still only *one* dependent and *one* independent variable
$$ y = a_0 + a_1x + a_2x^2 + ... + a_nx^n$$
- This allows for a nonlinear relationship between the variables
- This is still considered a linear model because the coefficients are linear
## Linear regression in machine learning
- A supervised learning algorithm
- Shows the *linear* relationship between:
    - The independent variable $X$ (predictor, input, features)
    - The dependent variable $Y$ (response, output, target)
- Tries to find the best fit line that describes the relationship between $X$ and $Y$
- In higher dimensions, it tries to find the best fit hyperplane
- Data comes in the form of $N$ input-output pairs
$$ D = \{(x^1, y^1), (x^2, y^2), ..., (x^N, y^N)\}$$
- Our system parameters are $w$ and $b$ (or $w_0$)
- For one dimension, the model is $y = wx + b$
- For $d$ dimensions, the model is
$$ y = w_0 + \sum_{j=1}^{d}w_jx_j$$
- In general:
    - The input dimension is $d \geq 1$
    - We have a *bias* term $w_0$
    - We have $d$ *weights*
$$ \textbf{w} = \begin{bmatrix} w_0 \\ w_1 \\ ... \\ w_d \end{bmatrix}$$
- Thus $w$ is a weight matrix
## Loss function
- The goal is to get the best values of $w$ and $b$
- The best fit line has the *least error*
- In regression, the error between the actual value $t$ and the predicted value $y$ is called the *residual* $\epsilon$
- $\epsilon = t - y$
- The loss function we want to minimize is $L = \frac{1}{2}(t - y)^2$
- For a given set of parameters $w$ and $b$, the cost function computes the total squared error over the entire dataset
$$ \mathcal{l}(w) = \sum_{n=1}^{N} [t^n - (w_0 + w_1 x^n)]^2$$
- When we minimize the cost function, we are finding the best parameters $w$
$$ \textbf{w}^* = \arg\min_{\textbf{w}} \mathcal{l}(\textbf{w})$$
## Minimization of the Least Squares Cost Function
- Let us introduce the matrix notation
    - $\textbf{X} = \begin{bmatrix} 1 \\ x \end{bmatrix}$
    - $\textbf{W} = \begin{bmatrix} b \\ w_1 \end{bmatrix}$
    - Here we treat the bias as another weight with input 1
- $\textbf{t} = [t^1, t^2, ..., t^N]^T \in \mathbb{R}^{N \times 1}$
- $\textbf{X} = \begin{bmatrix} 1 & x^1 \\ 1 & x^2 \\ ... & ... \\ 1 & x^N \end{bmatrix} \in \mathbb{R}^{N \times 2}$
- $\textbf{W} = \begin{bmatrix} w_0 \\ w_1 \end{bmatrix} \in \mathbb{R}^{2 \times 1}$
- Since $\textbf{Y} = \textbf{X}^T\textbf{W}$, we can write the loss function as
$$ \mathcal{l}(\textbf{w}) = \sum_{n=1}^{N} [t^n - \textbf{W}^T\textbf{X}^n]^2$$
- Then we can get rid of the summation by writing the loss function in matrix form
$$ \mathcal{l}(\textbf{w}) = (\textbf{X}\textbf{w} - \textbf{t})^T(\textbf{X}\textbf{w} - \textbf{t})$$
- Note that $\textbf{X}\textbf{w} - \textbf{t} \in \mathbb{R}^{N \times 1}$ and $(\textbf{X}\textbf{w} - \textbf{t})^T \in \mathbb{R}^{1 \times N}$
- Now we can solve for the optimal $\textbf{w}$ analytically
- First expand the loss function
$$ \begin{align*}
\mathcal{l}(\textbf{w}) &= (\textbf{X}\textbf{w} - \textbf{t})^T(\textbf{X}\textbf{w} - \textbf{t}) \\
&= \textbf{w}^T\textbf{X}^T\textbf{X}\textbf{w} - \textbf{t}^T\textbf{X}\textbf{w} - \textbf{w}^T\textbf{X}^T\textbf{t} + \textbf{t}^T\textbf{t} \\
&= \textbf{w}^T\textbf{X}^T\textbf{X}\textbf{w} - 2\textbf{t}^T\textbf{X}\textbf{w} + \textbf{t}^T\textbf{t}
\end{align*}$$
- Now we can take the partial derivative with respect to $\textbf{w}$ and set it to zero
$$ \begin{align*}
\frac{\partial}{\partial \textbf{w}} (\textbf{w}^T\textbf{X}^T\textbf{X}\textbf{w} - 2\textbf{t}^T\textbf{X}\textbf{w} + \textbf{t}^T\textbf{t}) &= 0 \\
(\textbf{X}^T\textbf{X})\textbf{w} - \textbf{X}^T\textbf{t} &= 0 \\
(\textbf{X}^T\textbf{X})\textbf{w} &= \textbf{X}^T\textbf{t} \\
\end{align*}$$
- Thus, we have a closed form solution of $\textbf{w} = (\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\textbf{t}$
- This is the same with multiple dimensions
- Summary:
    - Organize all the training samples into a matrix $\textbf{X}$ with one row per sample
    - Organize all the target values into a vector $\textbf{t}$
$$ \textbf{y} = \textbf{X}\textbf{w} + \textbf{b} \textbf{1} = \begin{pmatrix} \textbf{w}^T\textbf{x}^1 + b \\ \textbf{w}^T\textbf{x}^2 + b \\ ... \\ \textbf{w}^T\textbf{x}^N + b \end{pmatrix} = \begin{pmatrix} y^1 \\ y^2 \\ ... \\ y^N \end{pmatrix}$$
- Compute the squared error cost for the entire dataset
$$ \mathcal{J} = \frac{1}{2N} ||\textbf{t} - \textbf{y}||^2 $$
- In code:
```python
y = np.dot(X, w) + b
cost = np.sum((t - y) ** 2) / (2 * N)
```
## Gradient Descent
- Our second approach is using **gradient descent**
- Gradient descent looks at the error based on the current parameters and tries to find the direction to move to reduce the error
- Gradient points up the hill, so we move in the opposite direction
- The update rule is $w_j \leftarrow w_j - \alpha \frac{\partial}{\partial w_j} \mathcal{J}(\textbf{w})$
- The term $\alpha$ is the learning rate, similar to perceptron learning rate
- We often use gradient descent instead of the closed form solution because:
    - GD applies to a much broader set of models
    - GD may be easier to implement than direct solution
    - GD may be more efficient for high-dimensional data (matrix inversion is an $O(n^3)$ operation)
- The **mean squared error** is a common loss function for regression
$$ \text{MSE} = \frac{1}{N} \sum_{n=1}^{N} (t^n - \textbf{w}^T\textbf{x}^n)^2$$
- Gradient descent weights update rule:
    - Initialize $\textbf{w}$ randomly
    - Repeatedly update $\textbf{w}$ using the rule
$$ \textbf{w} \leftarrow \textbf{w} - \mu \frac{\partial}{\partial \textbf{w}} \mathcal{l}(\textbf{w})$$
- LMS: least mean squares aka Widrow-Hoff learning rule
## Basis functions
- Previously we assumed a linear relationship between the input and output
- We can extend regression by using **basis functions**
- Now we have a linear combination of nonlinear functions of the input variables
$$ y(x,w)