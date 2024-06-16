## Over/Under fitting
- To explain this we need to know what **performance** is
- **Performance** is based on:
    - Accuracy on training data
    - How well the model generalizes to new data not seen before
- There are two types of **errors** in machine learning models:
    - Irreducible error - cannot be reduced if you use the best model
    - Reducible error:
        - Square of bias and variance
        - Overfitting and underfitting are related to this
        - The given data is not enough to make a good model
### Fit
- Statistical fit
    - Describes fit statistically
    - Measures how well the model fits the data
    - Good fit if it converges
- Error: compare the model's prediction to the actual value
    - Training error: error on the training data
    - Test error: error on the test data
- **Bias**:
    - Measures the difference between the predicted value and the actual value
    - Higher bias indicates underfitting--the model is too simple
- **Variance**:
    - Measures the difference in the fits between different datasets
    - Higher variance indicates overfitting--the model loses generality
#### Bias and Variance tradeoff
- This is similar to the precision and accuracy dichotomy
    - Precision: how close the values are to each other
    - Accuracy: how close the values are to the target
- Models using a simple algorithm will have *high* bias and *low* variance (underfitting)
- Models using a complex algorithm will have *low* bias and *high* variance (overfitting)
- Ideally, we want a model with *low* bias and *low* variance
#### Overfitting
- Overfitting models produce good predictions on the training data but poor predictions on the test data
- This is also called not generalizing well
- The reason for this is that the model is too complex or the patterns in the training data aren't representative of the test data
#### Underfitting
- Underfitting models produce poor predictions on both the training and test data
- Oftentimes happens when the model is too simple to capture the underlying structure of the data
#### Detecting Overfitting and Underfitting
- How do we determine if a model is overfitting or underfitting?
- We can plot training error and validation error together (versus epochs)
    - In the beginning, both errors will decrease
    - Overfitting happens when validation loss increases but training loss decreases
- Detecting underfitting is easier: both errors will be high
- Choosing model complexity is a challenge when we don't know the underlying structure of the data
#### How do we fix Overfitting and Underfitting?
- Overfitting:
    - Reduce model complexity: complex models will have higher variance
    - Apply regularization to suppress higher-order terms
    - More training data
    - **Bagging**: train multiple models on different subsets of the data
- Underfitting:
    - Increase model complexity (kernelize, nonlinearize, ...)
    - Increase the number of passes over the data
    - Increase parameters
    - Add more features
    - **Boosting**: train multiple models sequentially, each model correcting the errors of the previous model

> Decreasing bias will increase variance and vice versa

## Cross-Validation
- Two-way holdout validation involves splitting the data into training and test sets
- The test set is new unseen data for the model, which is used to evaluate the model's performance
- Typically 2/3 of the data is used for training and 1/3 for testing
- Larger datasets can have smaller test sets
- Hyperparameters still need to be tuned manually
- Once the model is evaluated to be good, the model is trained on the entire dataset
- Holdout has some disadvantages:
    - The dataset may not be evenly distributed, so the test set may not be representative
    - The model may be overfitting the training set
    - The model might memorize the training data
### Repeat Holdout
- To mitigate the disadvantages of holdout, we can repeat the holdout process multiple times with different subsets of the data
- This can also be used for hyperparameter tuning
- Split the dataset into three parts: training, validation, and test
- Use the validation set to tune the hyperparameters and select the best model
- Reusing the test set would introduce bias, which is why we need a separate test set
### K-Fold Cross-Validation
- K-Fold Cross-Validation is a more robust method than holdout
- Prevents overlapping test sets
- Technique for model evaluation and selection
- The main idea is that each sample in the dataset has the opportunity of being tested
- K-fold cross validation is a special case of cross validation
    - The dataset is iterated over $k$ times
    - In each round the dataset is split into $k$ parts
        - One part is used for validation
        - The remaining $k-1$ parts are merged into a training set
- This will produce $k$ models with $k$ different performance metrics
- The final model is the average of the $k$ models
#### Special cases
- If $k$ is too small:
    - The pessimistic bias will be higher
    - Variance may be higher as well
- $k = 10$ is a common good choice
There are two special cases:
    $k = 2$: this is called the two-fold cross-validation
    $k = n$: this is called leave-one-out cross-validation
- 2-fold cross-validation is basically the same as holdout
- Leave-one-out cross-validation:
    - Set $k = n$
    - The number of folds = the number of training samples
    - This is computationally expensive
    - This is useful when the dataset is small, since withholding data would be wasteful
- Research has shown that 10-fold cross-validation is a good choice for most datasets
- Increasing the number of folds will:
    - Decrease bias
    - Increase variance
    - Increase computational cost
### Model Selection
- Apply k-fold cross-validation on each hyperparameter configuration
- This results in multiple models and performance metrics
- Then use all data to train the best model
## Regularization
- Regularization is a technique used to prevent overfitting
- In machine learning, regularization makes the objective function regular
- It adds some bias to the model
- Constrains the model so it cannot fit the noise
$$\begin{align*}
\text{Regularization} &= \text{Loss Function} + \text{Penalty} \\
&= L(\textbf{w}) + \lambda R(\textbf{w})
\end{align*}$$
### Regularized least squares
- Add a penalty term to the error function to discourage large weights
$$ E(b, w) = \frac{1}{2N} \sum_{i=1}^{N} (t^n - (w^T x^n + b))^2 + \frac{\lambda}{2} ||w||^2 $$
- Here our penalty term is the squared norm of the weights times a constant $\lambda$
- The constant $\lambda$ is a hyperparameter that adjusts the tradeoff between low training loss and low complexity
---
- The most common types of regularization are:
    - L1 regularization (Lasso) $\lambda ||w||$
    - L2 regularization (Ridge) $\frac{\lambda}{2} ||w||^2$
    - More data
    - Dropout
### L2 - Ridge Regularization
- With linear regression this is called Ridge regression
- Logistic regression typically uses L2 regularization by default
- L2 can be applied to other algorithms as well
    - Perceptron
    - Any gradient descent algorithm

$$ \mathcal{J}_{reg} = \mathcal{J} + \lambda \mathcal{R} = \mathcal{J} + \frac{\lambda}{2} \sum_{j} w_j^2 $$
$$ \mathcal{R} = \frac{1}{2} ||w||^2 = \frac{1}{2} \sum_{j} w_j^2 $$

- Choosing $\lambda$ comes to hyperparameter optimization
    - Positive values of $\lambda$ will reduce the weights
    - $\lambda = 0$ will not change the weights
    - As $\lambda \to \infty$, the weights will approach zero
- The modified gradient descent weight update rule is:

$$ w \leftarrow (1 - \mu \lambda) w - \mu \frac{\partial \mathcal{J}}{\partial w} $$

- The closed form solution for Ridge regression is:

$$ w = (\lambda I + X^T X)^{-1} X^T t $$

- Choosing the right $\lambda$ is important and will be difficult
    - Thus cross-validation is often used
    - Irrelevant features will have small but non-zero weights if $\lambda$ is good
### L1 - Lasso Regularization
- Least Absolute Shrinkage and Selection Operator is an alternative to L2 regularization for linear regression
- L1 regularization is used when there are unimportant features
- Often results in many weights being exactly zero