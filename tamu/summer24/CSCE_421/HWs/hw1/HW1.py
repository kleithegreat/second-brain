#CSCE 421

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from typing import Tuple, List


# ## complete the function below (to read data from csv)

def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def get_df_shape(df: pd.DataFrame) -> Tuple[int, int]:
    return df.shape


# ## Extract features 

def extract_features_label(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    features = df[['sepal.length', 'sepal.width']]
    label = df['variety']
    return features, label


#  ## Split the data into a train/test split

def data_split(features: pd.DataFrame, label:pd.Series, test_size:float
              ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    xtrain, xtest, ytrain, ytest = train_test_split(features, label, test_size=test_size)
    return xtrain, ytrain, xtest, ytest


# ## Write a function that returns score on test set with KNNs (use KNeighborsClassifier class)

def knn_test_score(n_neighbors:int, x_train: np.ndarray, y_train:np.ndarray, x_test: np.ndarray, y_test: np.ndarray) -> float:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(x_train, y_train)
    return knn.score(x_test, y_test)


# ## Apply k-NN to a list of data
# Let Variable accu denote a list of accuracy corresponding to k[1,2,..,10]. You can use previously used functions (if they are correct)

def knn_evaluate_with_neighbours(n_neighbors_min:int, n_neighbors_max:int, x_train: np.ndarray, y_train:np.ndarray, x_test: np.ndarray, y_test: np.ndarray) -> List[float]:
    ## Note neighbours_min, neighbours_max are inclusive
    accu = []
    for i in range(n_neighbors_min, n_neighbors_max+1):
        accu.append(knn_test_score(i, x_train, y_train, x_test, y_test))
    return accu


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    df = read_data('./iris.csv')
    
    shape = get_df_shape(df)
    
    features, label = extract_features_label(df)

    x_train, y_train, x_test, y_test = data_split(features, label, 0.33)

    print(knn_test_score(1, x_train, y_train, x_test, y_test))

    acc = knn_evaluate_with_neighbours(1, 10, x_train, y_train, x_test, y_test)
    
    plt.plot(range(1,11), acc)
    plt.show()


