import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
    filtered_df = df[df['variety'].isin(['Setosa', 'Virginica'])]
    # Extract the required features and labels from the filtered dataframe
    features = filtered_df[['sepal.length', 'sepal.width']]
    labels = filtered_df['variety'].map({'Setosa': -1, 'Virginica': 1})
    return features, labels

def cost(w, C, margin):
    #cots=(1/2)ww+C*SUM(max(0,1-margin))
    
    ### YOUR CODE HERE

    pass

def decision_function(w,b, X):
    ##decision=Xw+b
    ### YOUR CODE HERE

    pass

def margin(w,b, X, y):
    #margin=y(Xw+b)
    
    ### YOUR CODE HERE

    pass
    

class LinearSVM:
    def __init__(self, C=1.0):
        self.C = C

        self._support_vectors = None
        self.margin_array = []
        self.loss_array = []

    def fit(self, X, y, lr=0.001, epochs=1000):
        # Initialize w and b
        self.n, self.d = X.shape
        self.w = np.random.randn(self.d)
        self.b = 0
        ynew = np.where(y <= 0, -1, 1)
        
        ### YOUR CODE HERE

        return self.loss_array, self._support_vectors, self.margin_array

    def predict(self, X):
        #sign(decision_function(..))
        ### YOUR CODE HERE

        pass

    def score(self, X, y):
        P = self.predict(X)
        score = 0.00

        ### YOUR TRAIN SCORE CODE HERE

        return P, score
        
    def plot_decision_boundary(self, X,y):
        plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap=plt.cm.Paired, alpha=.5)
        ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        # create grid to evaluate model
        xx = np.linspace(xlim[0], xlim[1], 30)
        yy = np.linspace(ylim[0], ylim[1], 30)
        YY, XX = np.meshgrid(yy, xx)
        xy = np.vstack([XX.ravel(), YY.ravel()]).T
        Z = decision_function(self.w,self.b, xy).reshape(XX.shape)

        # plot decision boundary and margins
        ax.contour(XX, YY, Z, colors=['r', 'b', 'r'], levels=[-1, 0, 1], alpha=0.8,
                   linestyles=['--', '-', '--'], linewidths=[2.0, 2.0, 2.0])

        # the support vectors
        sv = np.where(margin(self.w, self.b, X, y) <= 1)[0]
        ax.scatter(X[:, 0][sv], X[:, 1][sv], s=100,
                   linewidth=1, facecolors='none', edgecolors='g')

        plt.show()


if __name__ == '__main__':
     
    df = read_data("./iris.csv")
    features, label = extract_features_label(df)
    X_train, y_train, X_test, y_test = data_split(features, label, 0.6)
    X_train, y_train, X_test, y_test = X_train.values, y_train.values, X_test.values, y_test.values

    # soft-margin SVM
    model = LinearSVM(C=0.1)
    #Model training
    model.fit(X_train, y_train)
    #test the results
    print("train score:", model.score(X_test, y_test)[1])
    #plot the decision boundary for test data
    model.plot_decision_boundary(X_test, y_test)
    #model.plot_cost_function(X_test, y_test)
   # model.plot_decision_boundary(X_train, y_train)
