# Naive Bayes
- Previously, the perceptron used features to classify data
- We have two approaches to classification:
    - Discriminative: We estimate the parameters of a **decision boundary** or class separator directly from labeled data
        - Learning $P(t|x)$ directly (logistic regression, perceptron)
        - Learn mappings from inputs to classes
        - Attempts to solve the issue of separating classes
    - Generative: We model the distribution of input characteristics of each class
        - Build a model for the underlying features of each class
        - Build a model of $P(x|t)$ using Bayes' rule
        - Attempts to solve the issue of what each class "looks like"
- Some machine learning methods of discriminative classifiers:
    - KNN
    - Logistic regression
    - SVM
    - Decision trees
    - Random forest
    - Neural networks
- Instead of attempting to separate classes, we attempt to model the distribution of input characteristics of each class in Naive Bayes
- Generative models allow us to generate new data (e.g. generate a cat image)
- The **Naive Bayes** algorithm is a *supervised* learning algorithm based on **Bayes' Theorem**
    - Used for classification
    - A **probabilistic** classifier--predicts on the basis of the probability of an object belonging to a certain class
    - Examples: spam filtering, sentiment analysis, classifying articles
- Etymology:
    - Naive: The algorithm assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature
    - Bayes: The algorithm is based on Bayes' Theorem
## Probability
- Predict how likely some event $E$ is to occur, considering the total number of possible outcomes
$$P(E) = \frac{\text{Number of ways event E can occur}}{\text{Total number of possible outcomes}}$$
- Conditional probability: The probability of an event given that another event has occurred
- Need two or more events
- The conditional probability of event $E2$ given event $E1$ is:
$$P(E2|E1) = \frac{P(E1 \cap E2)}{P(E1)}$$
### Bayes' Theorem
- A way of determining the probability of a hypothesis given prior knowledge
- Depends on conditional probabilities
- Bayes' Theorem:
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
- Where:
    - $P(A|B)$: The probability of event $A$ given event $B$
    - $P(B|A)$: The probability of event $B$ given event $A$
    - $P(A)$: The probability of event $A$
    - $P(B)$: The probability of event $B$
    - There is no correlation between $P(A)$ and $P(B)$
### Bayes' Theorem in Machine Learning
- We can adapt Bayes' Theorem to classify data
- Bayes' Theorem then becomes a probability model where:
$$ P(C = k|X) = \frac{P(X|C = k)P(C = k)}{P(X)} $$
- Where:
    - $C$ is a variable representing the class of the data
    - $X$ is the training data $X = (x_1, x_2, ..., x_m)$
    - $k$ is the specific class (current class)
- $P(C = k|X)$ is the **posterier**
    - This is the probability of the output class $C=k$ given the input data $X$
    - To be *predicted* from test data
- $P(X|C = k)$ is the **likelihood**
    - This is the probability of the input data $X$ given the output class $C=k$
    - Known/esitmated from training data
- $P(x)$ is the probability of $X$
- $P(C = k)$ is the **prior**, or initial probability of a class
- The idea of Naive Bayes is to use $P(X|C = k)$ and $P(C = k)$ to predict $P(C = k|X)$
## Algorithm
- Given the feature vectors of data we want to classify, we want to know the probability of each class
- Start with $P(C = k)$, the initial probability of a class
- This is calculated as:
$$P(C = k) = \frac{N_k}{N}$$
- Where $N_k$ is the number of training data points in class $k$ and $N$ is the total number of training data points
- Next, we calculate $P(X|C = k)$, the likelihood of the input data given the output class
- This is calculated as:
$$P(X|C = k) = \frac{N_{xi, k}}{\Sigma N_{X, C}}$$
- Where:
    - $N_{xi, k}$ is the number of occurrences of feature $x_i$ in class $k$
    - $\Sigma N_{X, C}$ is the total number of occurrences of all features in class $k$
- In a two class problem, we can calculate the probability of a class given the input data as:
$$ P(X) = P(X|C = 0)P(C = 0) + P(X|C = 1)P(C = 1) $$
- Finally, we can estimate the class
$$ \hat{k} = P(C = k|X) = \frac{P(X|C = k)P(C = k)}{P(X)} $$
- Since $P(X)$ is the same for all classes, we can ignore it
$$ \begin{align*}
\hat{k} &= \text{argmax} P(C = k|X) \\
&= \text{argmax}_{k \in C} P(X|C = k)P(C = k) 
\end{align*}$$
- In other words, we choose the class that maximizes the **likelihood** times the **prior**
- There is also a log version for numerical stability
$$ \hat{k} = \text{argmax}_{k \in C} \log P(C = k) + \sum_{i=1}^m \log P(X|C = k) $$
- Using the chain rule, we can rewrite the likelihood as:
$$ \begin{align*}
P(X|C = k) P(C = k) &= P(x_1, x_2, ..., x_m, C = k) P(C = k) \\
&= P(x_1 | x_2, ..., x_m, C = k) P(x_2, ..., x_m, C = k) P(C = k) \\
&= \cdots \\
&= P(x_1 | x_2, ..., x_m, C = k) P(x_2 | x_3, ..., x_m, C = k) \cdots P(x_m | C = k) P(C = k)
\end{align*}$$
- For binary classification, there are $(2^m - 1) \times k$ parameters to estimate
    - $m$ is the number of features
    - $k$ is the number of classes
- Using the assumption that features are independent, we can simplify the likelihood
$$ \begin{align*}
P(X|C = k) &= P(x_1 | x_2, ..., x_m, C = k) P(x_2 | x_3, ..., x_m, C = k) \ldots P(x_m | C = k) \\
&= P(x_1 | C = k) P(x_2 | C = k) \cdots P(x_m | C = k) \\
&= \prod_{i=1}^m P(x_i | C = k)
\end{align*}$$
- Thus the Naive Bayes classifier becomes
$$ P(C = k|X) = \frac{P(C = k)}{P(X)} \prod_{i=1}^m P(x_i | C = k) $$
- Where:
    - $P(X) = \sum_1^k P(x_i)$
    - The number of parameters to estimate is $m \times k$
> Conditional independence oftentimes does not hold in practice. However, the Naive Bayes classifier is still effective on many problems and serves as a decent baseline for more sophisticated models.
- Finally, we can drop the denominator $P(X)$ since it is not dependent on $k$, so we can rewrite the classifier as:
$$ \hat{k} = \text{argmax}_{k \in C} P(C = k) \prod_{i=1}^m P(x_i | C = k) $$
- There are two ways to estimate the parameters:
    - **MLE (Maximum Likelihood Estimation)**: Estimate the parameters by maximizing the likelihood of the training data
        - Defined as $\hat{\theta}_{MLE} = \text{argmax}_{\theta} P(D|\theta)$
        - This is $\text{argmax}_{k \in C} \prod_{i=1}^m P(x_i | C = k)$
    - **MAP (Maximum A Posteriori)**: Estimate the parameters by maximizing the posterior probability of the parameters given the data. 
        - Defined as $\hat{\theta}_{MAP} = \text{argmax}_{\theta} P(\theta|D)$
        - This is $\text{argmax}_{k \in C} P(C = k) \prod_{i=1}^m P(x_i | C = k)$
## Laplace Correction/Smoothing
- The *likelihood* $P(x_i | C = k)$ is calculated for each feature $x_i$ in class $C$
- If a feature does not appear in the training data for a class, the likelihood will be zero
- This will cause the entire probability to be zero
- Normally, having a zero probability for a feature is not a problem
- However, if we have many features, we may encounter a zero probability for a class
- To avoid this, we can use **Laplace smoothing**
- Laplace smoothing adds a small value to the numerator and denominator of the likelihood
$$ P(x_i | C = k) = \frac{N_{xi, k} + 1}{\Sigma N_{X, C} + V} $$
- Where $V$ is the number of possible feature values
## Gaussian Naive Bayes
- We want to use Naive Bayes with continuous features
- The **probability density function (pdf)** describes the probability of a random variable taking on a certain value
- The **Gaussian** or **normal distribution** is the most common model for continuous random variables whose distributions are not known
- The Gaussian distribution is defined by two parameters:
    - The mean $\mu$ (average)
    - The variance $\sigma^2$ (spread)
$$ p(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) $$
- To use Naive Bayes with continuous features, just replace $P(x_i | C = k)$ with the Gaussian distribution
$$ P(x_i | C = k) = \frac{1}{\sqrt{2\pi\sigma^2_{k}}} \exp\left(-\frac{(x - \mu_{k})^2}{2\sigma^2_{k}}\right) $$