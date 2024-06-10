import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from typing import Tuple, List
import sklearn.linear_model

# Download and read the data.
def read_train_data(filename: str) -> pd.DataFrame:
    '''
        read train data and return dataframe
    '''
    return pd.read_csv(filename)

def read_test_data(filename: str) -> pd.DataFrame:
    '''
        read test data and return dataframe
    '''
    return pd.read_csv(filename)


# Prepare your input data and labels
def prepare_data(df_train: pd.DataFrame, df_test: pd.DataFrame) -> tuple:
    '''
        Separate input data and labels, remove NaN values. 
        Execute this for both dataframes.
        return tuple of numpy arrays(train_data, train_label, test_data, test_label).
        may use .dropna, 
    '''
    dr_train = df_train.dropna()
    dr_test = df_test.dropna()

    x_train = dr_train['x'].values
    y_train = dr_train['y'].values

    x_test = dr_test['x'].values
    y_test = dr_test['y'].values

    return x_train, y_train, x_test, y_test

# Implement LinearRegression class
class LinearRegression:   
    def __init__(self, learning_rate=0.01, epoches=1000):        
        self.learning_rate = learning_rate
        self.iterations    = epoches
        self.W = None
        self.b = None
          
    # Function for model training         
    def fit(self, X, Y):
        # weight initialization
        self.N, self.n = X.shape     
        self.W = np.zeros((self.n, 1))          
        self.b = 0
        ### YOUR CODE HERE

        ### YOUR CODE HERE   
        
        # data
        ### YOUR CODE HERE 
        
        # gradient descent learning                  
        ### YOUR CODE HERE
        ## GRADIENT UPDATE, UPDATE USING ALL TRAINING SET 
        # predict on data and calculate gradients 
        ### YOUR CODE HERE

        ### YOUR CODE HERE  
          
        # update weights
        ### YOUR CODE HERE
        pass

      
    # output      
    def predict(self, X):
        ### YOUR CODE HERE

        ### YOUR CODE HERE 
        pass

# Calculate and print the mean square error of your prediction
def MSE(y_test, pred):
    '''
        return the mean square error corresponding to your prediction
    '''
    return np.sum((y_test - pred)**2) / len(y_test)



if __name__ == "__main__":
   
    data_path_train   = "./train2.csv"
    data_path_test    = ".test.csv"
    df_train, df_test = read_train_data(data_path_train), read_test_data(data_path_test)


    train_X, train_y, test_X, test_y = prepare_data(df_train, df_test)
    r = LinearRegression(learning_rate=0.0001, epoches=10)
    r.fit(train_X, train_y)

    #print?
    print(df_train.head())
    print(df_test.head())

    # Make prediction with test set
    preds = r.predict(test_X)
    print(preds.shape)
    print(test_y.shape)
    # Calculate and print the mean square error of your prediction
    mean_square_error = MSE(test_y, preds[:,1])
    print(mean_square_error) # I added this

    # plot your prediction and labels, you can save the plot and add in the report
    plt.scatter(test_X,test_y, label='data')
    plt.plot(test_X, preds)
    plt.legend()
    plt.show()

    
