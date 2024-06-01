# k-nearest neighbors
- K-nearest neighbors is a *supervised* machine learning algorithm
- It can be used for both classification and regression problems
    - **Classification** problems have discrete outputs
    - **Regression** problems have real valued outputs
    - KNN is mostly used for classification
- KNN works under the assumption that similar things exist in close proximity
## Example - cats and dogs
- Suppose we have an image of either a cat or a dog
- We can use KNN to determine which one it is
- We can say that cats tend to have smaller noses and pointy ears
- KNN will find the $k$ nearest labeled samples
### Similarity and Dissimilarity
- **Similarity** is a measure of how alike two data objects are
    - Has a value in the range $[0, 1]$
    - Higher when more similar
- Proximity mesures similarity
## KNN
- Find the $k$ nearest neighbors for a given point
    - Use the class labels in the case of classification
    - Use their values in the case of regression
- 1-NN uses one target that is closest to the input
- k-NN uses a combination of the $k$ closest training samples
- KNN is also a lazy learning algorithm
- The dataset can be represented by $D = (\textbf{x}, t)$
    - Here $D$ is the dataset
    - $\textbf{x}$ is the feature vectors
    - $t$ is the labels
- KNN requires a distance metric and a value of $k$
- The output will be based on either the majority class or mean value of k nearest neighbors
- The upshot: KNN requires three things:
    - Set of training samples
    - A distance metric
    - Some value for $k$
- $k$ is typically a small positive integer
## Training and learning
- KNN doesnt learn parameters--it simply memorizes the training set
- KNN goes through the following steps:
    1. Calculate distnace (find the distance between the input vector and all training data)
    2. Find the $k$ nearest neighbors
    3. Use the $k$ nearest neighbors to make a prediction
## KNN Pseudocode
```
Initialize k
Choose distance metric
For v in training dataset:
    Calculate the distance between the input vector and v
    Add this distance to an ordered collection of all distances
    Sort the ordered collection of distances
Pick the first $k$ entries from the sorted collection
Get the labels of the selected $k$ entries
If regression:
    return the means of the $k$ labels
If classification:
    return the mode of the $k$ labels
```
## Summary
- KNN is:
    - Instance based learning
    - Non-generalizing learning
    - Lazy learning
- KNN does not focus on constructing a general internal model
> KNN has no actual learning in some sense
## Choosing a value for $k$
- Larger values of $k$ will lead to smoother decision boundaries
- $k$ is a hyperparameter
- Important for the performance of KNN
- Small values of $k$ will be too sensitive to noise and lead to overfitting
- Large values of $k$ may oversimplify decision boundaries and fail to capture important patterns in the data (underfitting)
- **Overfitting** is when the model performs well on training data but poorly on test data
- **Underfitting** is when the model performs poorly on both training and test data
- Choosing a good value of $k$ depends on the specific dataset and what problem you are trying to solve
- Generally:
    - Smaller values of $k$ will have more complex decision boundaries, and capture fine-grained patterns
    - Larger values of $k$ makes stable predictions over lots of examples
> Rule of thumb: $k < \sqrt{n}$ where $n$ is the number of samples in the dataset
- We can use *cross validation* to find the best value of $k$
    - Split the dataset into training and test sets multiple times
    - Train and evaluate the model on each split for different values of $k$
- Our distance metric is another hyperparameter
- The most common distance metrics are:
    - Euclidean distance (p2 norm)
    - Manhattan distance (p1 norm)
    - Minkowski distance (p norm)
    - Hamming distance (for categorical data, counts the number of positions at which the corresponding symbols are different)
## Performance metrics
- Common performance metrics for classification problems:
    - Accuracy
    - Precision
    - Recall
    - F1 score
    - ROC AUC
    - PR AUC
- Common performance metrics for regression problems:
    - MSE (mean squared error)
    - RMSE (root mean squared error)
    - MAE (mean absolute error)
    - R2 (coefficient of determination)
## Limitations of KNN
- **Curse of dimensionality**
    - Distance between points becomes less meaningful in higher dimensions
    - This is due to volume of the space increasing exponentially with the number of dimensions, leading to sparsity
    - This can make it difficult to find a reliable set of neighbors
- Imbalanced data set
    - Suppose there is some minority class that is sparse and scattered, while the majority class dominates the feature space
    - The distances between the minority class samples will be larger than the distances between the majority class samples
    - This can lead to misclassification of the minority class
- Computationally expensive
    - Computational complexity depends on:
        - Size of dataset
        - Number of features
        - Value of $k$
    - KNN becomes impractical for large datasets
    - Time complexity for a single query point is $O(nd)$ where $n$ is the number of samples and $d$ is the number of features
    - Total time complexity is $O(knd)$
## Improving KNN
- To reduce the runtime:
    - One method is to use a branch and bound technique, eliminating the need to calculate the distance to all points
    - Another method is to use a KD tree (offline computation), each node represents a k-dimensional point
    - Use locality-sensitive hashing to hash similar points to the same buckets with high probability
- Feature selection takes a subset of relevant features from the main dataset, and aims to remove irrelevant and redundant features
- Dimensionality reduction techniques can find a lower-dimensional space that preserves the essential structure of the data
- One example is PCA (principal component analysis), and it works by projecting the data onto a lower-dimensional space (linear combination of the original features)
- Ensemble methods combine the predictions of multiple models
    - One way is called **bagging**
        - Multiple models are trained on different subsets of the data
        - The final prediction is the average of the predictions of all models
    - Another way is called **boosting**
        - Models are trained sequentially
        - Each model tries to correct the errors of the previous model
- Feature scaling can improve the performance of KNN
    - Some attributes may have a larger range of values than others
    - We can avoid bias towards one attribute by scaling all attributes to the same range
    - z-score normalization is one way to scale the data: $x_i \leftarrow \frac{x_i - \mu}{\sigma}$
        - Represents the feature value in terms of the standard deviation and mean
        - Good for normally distributed data
    - Min-max scaling is another way to scale the data: $x_i \leftarrow \frac{x_i - \min(x)}{\max(x) - \min(x)}$
        - Also called unity-based normalization
        - All features will be in the range $[0, 1]$
- We can **assign weights** to certain attributes which we believe are more important
    - If we know that some attributes are more important than others, we can assign them higher weights
    - Higher weights give more importance to the attribute
- We can tune the hyperparameter $k$ using a validation set