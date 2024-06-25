# Logistic Regression
- Logisic regression is a modification of linear regression
    - Deals with binary categories or outcomes
    - Relates independent variables $x_1, x_2, \ldots, x_n$ to a binary dependent variable $y$
    - Is a discriminative model
- Features can be continuous or categorical
- Outcome is discrete
- For data with continuous features and a binary outcome, there is no obvious way to use linear regression
- To solve this, we use the logit transformation:
$$ s(z) = \frac{1}{1 + e^{-z}} $$
- This maps real values to the range $[0, 1]$
- The regression line is transformed to a sigmoid curve
- This gives the probability of the outcomes
- Logistic regression learns the decision boundary by estimating $P(Y | X)$ directly from the data
$$ P(Y = 1 | X) = \frac{1}{1 + \exp(w_0 + \sum_{i=1}^n w_i X_i)} $$
- To use the maximum liklihood, we need to assume a probability distribution
- In logistic regression we assume a binomial distribution, where each example is one outcome of a Bernoulli trial
- The bernoulli distribution is parameterized only by the probability of success $p$
    - $P(Y = 1) = p$
    - $P(Y = 0) = 1 - p$
- Thus, we can create a pdf representing a single experiment
$$ Y \sim \text{Bernoulli}(\theta), Y \in \{0, 1\} $$
$$ p(y | x, w) = \text{Ber}(y | p(w^T x)) $$
- The output belongs to class 1 with likelihood $p(w^T x)$