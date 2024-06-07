import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# read_data, get_df_shape, data_split are the same as HW2
def read_data(filename: str) -> pd.DataFrame:
    d = pd.read_csv(filename)
    df = pd.DataFrame(data=d)
    return df

class GaussianNaiveBayes:
    def __init__(self, eps=1e-6):
        self.classes = None
        self.mean = None
        self.var = None
        self.priors = None
        self.eps = eps  # small constant to avoid division by zero

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Train the Gaussian Naive Bayes model. Calculate the mean, variance, and prior probabilities for each class.
                             !!!!!ADD self.eps to self.var----> WHY?
        Parameters:
        X : np.ndarray
            The training features
        y : np.ndarray
            The training labels
            
        Returns:
        mean : np.ndarray
              The mean for each class
        var : np.ndarray
              The variance for each class
        priors : np.ndarray
              The prior probabilities for each class
        """
        self.classes = np.unique(y)
        
        num_classes = len(self.classes)
        num_features = X.shape[1]

        self.mean = np.zeros((num_classes, num_features))
        self.var = np.zeros((num_classes, num_features))
        self.priors = np.zeros(num_classes)

        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.mean[i] = X_c.mean(axis=0)
            self.var[i] = X_c.var(axis=0) + self.eps
            self.priors[i] = X_c.shape[0] / X.shape[0]
        
        return self.mean, self.var, self.priors
        

    def gaussian_probability(self, x: np.ndarray, mu: np.ndarray, sigma2: np.ndarray) -> np.ndarray:
        """
        Compute the Gaussian probability.

        Parameters:
        x : np.ndarray
            The input features
        mu : np.ndarray
            The mean values
        sigma2 : np.ndarray
            The variance values

        Returns:
        np.ndarray
            The Gaussian probabilities
        """
        return (1 / np.sqrt(2 * np.pi * sigma2)) * np.exp(-1 * (x - mu)**2 / (2 * sigma2))

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions for given features using the trained Gaussian Naive Bayes model.
                              !!!!!!USE log in claculations------>WHY?
        Parameters:
        X : np.ndarray
            The features to predict

        Returns:
        np.ndarray
            The predicted classes
        """
        num_samples = X.shape[0]
        num_classes = len(self.classes)
        
        posteriors = np.zeros((num_samples, num_classes))

        for i, c in enumerate(self.classes):
            prior = np.log(self.priors[i])
            class_conditional = np.sum(np.log(self.gaussian_probability(X, self.mean[i], self.var[i])), axis=1)
            posteriors[:,i] = prior + class_conditional

        return self.classes[np.argmax(posteriors, axis=1)]


def visualization(df: pd.DataFrame):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(35, 10))
    fig.suptitle("Data Visualization", fontsize=15)

    X = np.asarray(df.drop('variety', axis=1))
    x1, x2, x3, x4 = X.T[0], X.T[1], X.T[2], X.T[3]

    ax1.scatter(x1[:50], x2[:50], c='red')
    ax1.scatter(x1[50:100], x2[50:100], c='blue')
    ax1.scatter(x1[100:150], x2[100:150], c='green')
    ax1.set(xlabel='Sepal Length', ylabel='Sepal Width')

    ax2.scatter(x3[0:50], x4[0:50], c='red')
    ax2.scatter(x3[50:100], x4[50:100], c='blue')
    ax2.scatter(x3[100:150], x4[100:150], c='green')
    ax2.set(xlabel='Petal Length', ylabel="Petal Width")

    ax3.scatter(x1[:50]/x2[:50], x3[0:50]/x4[0:50], c='red')
    ax3.scatter(x1[50:100]/x2[50:100], x3[50:100]/x4[50:100], c='blue')
    ax3.scatter(x1[100:150]/x2[100:150], x3[100:150]/x4[100:150], c='green')
    ax3.set(xlabel='Sepal Length/Width', ylabel='Petal Length/Width')

    ax1.legend(['Iris-Setosa', 'Iris-Versicolor',
               'Iris-Virginica'], fontsize=15)
    ax2.legend(['Iris-Setosa', 'Iris-Versicolor',
               'Iris-Virginica'], fontsize=15)
    ax3.legend(['Iris-Setosa', 'Iris-Versicolor',
               'Iris-Virginica'], fontsize=15)

    plt.show()


# Testing
if __name__ == "__main__":
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    # Read the data
    train_df = read_data("./iris_training_data.csv")
    test_df = read_data("./iris_testing_data.csv")

    # Visualization for you to understand the data, you can comment it out
    # visualization(train_df)

    # Data preprocessing
    train_features = train_df.drop('variety', axis=1).values
    train_labels = train_df['variety'].values

    test_features = test_df.drop('variety', axis=1).values
    test_labels = test_df['variety'].values

    # Get the number of features
    num_features = train_features.shape[1]

    # Initialize and train the Naive Bayes classifier
    nb = GaussianNaiveBayes()
    nb.fit(train_features, train_labels)

    # Make predictions on the test set
    test_predictions = nb.predict(test_features)

    # Calculate accuracy
    accuracy = accuracy(test_labels, test_predictions)
    print("Naive Bayes Classification Accuracy: {:.2f}%".format(
        accuracy * 100))
