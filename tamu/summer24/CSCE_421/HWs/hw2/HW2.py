import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# read_data, get_df_shape, data_split are the same as HW2-kNN
def read_data(filename: str) -> pd.DataFrame:
    d = pd.read_csv(filename)
    df = pd.DataFrame(data=d)
    return df

def get_df_shape(df: pd.DataFrame) -> Tuple[int, int]:
    return df.shape

def data_split(
    features: pd.DataFrame, label: pd.Series, test_size: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=test_size)
    return X_train, y_train, X_test, y_test


def extract_features_label(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    # Filter the dataframe to include only Setosa and Virginica rows
    # Extract the required features and labels from the filtered dataframe
    filtered = df[df["variety"].isin(["Versicolor", "Virginica"])]
    features = filtered[["sepal.length", "sepal.width"]]
    label = filtered["variety"]
    label = label.replace({"Versicolor": 0, "Virginica": 1})
    return features, label

class Perceptron:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.activation = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Train the perceptron on the given input features and target labels.
        You need to do following steps:
        1. Initialize the weights and bias (you can initialize both to 0)
        2. Calculate the linear output (Z) of the perceptron for all the points in X
        3. Apply the activation function to Z and get the predictions (Y_hat)
        4. Calculate the weight update rule for the perceptron and update the weights and bias
        5. Repeat steps 2-4 for 'epochs' number of times
        6. Return the final weights and bias
        Args:
            X (array-like): The input features.
            y (array-like): The target labels.

        Returns:
            weights (array-like): Learned weights.
            bias (float): Learned bias.
        """
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        errors = [0]

        for _ in range(self.epochs):
            epoch_error = 0
            for xi, t in zip(X, y):
                y_hat = self.activation(np.dot(self.weights, xi) + self.bias)
                if y_hat != t:
                    epoch_error += 1
                    self.weights += self.learning_rate * (t - y_hat) * xi
                    self.bias += self.learning_rate * (t - y_hat)
            errors.append(errors[-1] + epoch_error)
        
        return errors


    def predict(self, X):
        """
        Predict the labels for the given input features.

        Args:
            X (array-like): The input features.

        Returns:
            array-like: The predicted labels.
        """
        y_hat = [self.activation(np.dot(self.weights, xi) + self.bias) for xi in X]
        return y_hat

    def _unit_step_func(self, x):
        """
        The unit step function, also known as the Heaviside step function.
        It returns 1 if the input is greater than or equal to zero, otherwise 0.

        Args:
            x (float or array-like): Input value(s) to the function.

        Returns:
            int or array-like: Result of the unit step function applied to the input(s).
        """
        return np.where(x >= 0, 1, 0)


# Testing
if __name__ == "__main__":
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy
    
    df=read_data("./iris.csv")
    shape = get_df_shape(df)
    features, label = extract_features_label(df)
    X_train, y_train, X_test, y_test = data_split(features, label, 0.2)
    X_train, y_train, X_test, y_test = X_train.values, y_train.values, X_test.values, y_test.values

    epoch_list = [1000]
    learning_rates = [0.01]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train)

    for epoch in epoch_list:
        for lr in learning_rates:
            p = Perceptron(learning_rate=lr, epochs=epoch)
            errors = p.fit(X_train, y_train)
            predictions = p.predict(X_test)
            print("Perceptron classification accuracy", accuracy(y_test, predictions))

            x0_1 = np.amin(X_train[:, 0])
            x0_2 = np.amax(X_train[:, 0])

            x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
            x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

            ax.plot([x0_1, x0_2], [x1_1, x1_2], label=f"Epochs: {epoch}, Learning Rate: {lr}")
            #ax.plot(range(len(errors)), errors)

    ymin = np.amin(X_train[:, 1])
    ymax = np.amax(X_train[:, 1])
    ax.set_ylim([ymin, ymax])
    # ax.legend()

    plt.show()
