import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from typing import Tuple, List

def MSE(y_test, pred):
    '''
        return the mean square error
    '''
    return metrics.mean_squared_error(y_test, pred)

def prepare_data(df_train: pd.DataFrame, df_test: pd.DataFrame) -> tuple:
    '''
        Separate input data and labels, remove NaN values. 
        Execute this for both dataframes.
        return tuple of numpy arrays(train_data, train_label, test_data, test_label).
    '''
    df_train_na_dropped = df_train.dropna()
    df_test_na_dropped = df_test.dropna()

    x_train = df_train_na_dropped['x'].to_numpy()
    x_train = x_train.reshape(x_train.shape[0], 1)

    y_train = df_train_na_dropped['y'].to_numpy()
    y_train = y_train.reshape(y_train.shape[0], 1)

    x_test  = df_test_na_dropped['x'].to_numpy()
    x_test = x_test.reshape(x_test.shape[0], 1)

    y_test  = df_test_na_dropped['y'].to_numpy()
    y_test = y_test.reshape(y_test.shape[0], 1)

    return x_train, y_train, x_test, y_test

# Download and read the data.
def split_data(filename: str, percent_train: float) -> pd.DataFrame:
    '''
        Given the data filename and percentage of train data, split the data
        into training and test data. 
    '''
    df_train = pd.DataFrame()
    df_test = pd.DataFrame()

    ### YOUR CODE HERE

    return df_train, df_test

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
        ### YOUR CODE HERE

        # data
        ### YOUR CODE HERE 
        
        # gradient descent learning                  
        ### YOUR CODE HERE

        # predict on data and calculate gradients 
        ### YOUR CODE HERE
          
        # update weights
        ### YOUR CODE HERE
        pass

      
    # output      
    def predict(self, X):
        predictions = np.zeros([np.shape(X)[0], np.shape(X)[0]])

        ### YOUR CODE HERE

        return predictions

class RidgeRegression(): 
      
    def __init__(self, learning_rate=.00001, iterations=1000, penalty=1) : 
          
        self.learning_rate = learning_rate         
        self.iterations = iterations         
        self.penalty = penalty 
          
    # Function for model training             
    def fit(self, X, Y) :       
        # weight initialization         

        # gradient descent learning   
          
        # calculate gradients       
 
        # update weights     
        pass    

    def predict(self, X):     
        predictions = np.zeros([np.shape(X)[0], np.shape(X)[0]])

        ### YOUR CODE HERE

        return predictions

def kFold(folds: int, data: pd.DataFrame):
    '''
        Given the training data, iterate through 10 folds and validate 
        10 different Ridge Regression models. 

        Returns:
            mse_avg - Float value of the average MSE between the models. 
            min_model - Integer index of the model with the minimum MSE in models[].
            models - List containing each RidgeRegression() object.
            min_mse - Float value of the minimum MSE. 
    '''   
    models = []

    ### YOUR CODE HERE

    return mse_avg, min_model, models, min_mse


if __name__ == "__main__":

    data_path = "./data.csv"
    df_train, df_test = split_data(data_path, .80)
    
    train_X, train_y, test_X, test_y = prepare_data(df_train, df_test)
    lr = LinearRegression(learning_rate=0.0001, epoches=10)
    lr.fit(train_X, train_y)

    # Make prediction with test set
    lr_preds = lr.predict(test_X)

    # Calculate and print the mean square error of your prediction
    lr_mean_square_error = MSE(test_y, lr_preds[:, :1])
    print("Normal Linear Regression MSE:")
    print(lr_mean_square_error) 

    #plot your prediction and labels, you can save the plot and add in the report
    plt.scatter(test_X,test_y, label='data')
    plt.plot(test_X, lr_preds, color='purple')
    plt.legend()
    plt.show()

    # Ridge Regression
    rd = RidgeRegression()
    rd.fit(train_X, train_y)
    rd_preds = rd.predict(test_X)
    rd_mean_square_error = MSE(test_y, rd_preds[:, :1])
    print("Adding a regularizer : Ridge Regression MSE:")
    print(rd_mean_square_error)

    #plot your prediction and labels, you can save the plot and add in the report
    plt.scatter(test_X,test_y, label='data')
    plt.plot(test_X, rd_preds, color='black')
    plt.legend()
    plt.show()


    # df_train, df_test = split_data(data_path, .80)
    kFold_train_X, kFold_train_y, kFold_test_X, kFold_test_y = prepare_data(df_train, df_test)
    mse_avg, min_model, models, mse_min = kFold(10, df_train)
    best_model = models[min_model]
    
    print("KFold Ridge Regression MSE Average:")
    print(mse_avg)
    
    print("KFold Ridge Regression MSE Best Model:")
    print(mse_min)

    kFold_preds = best_model.predict(kFold_test_X)
    kFold_mean_square_error = MSE(kFold_test_y, kFold_preds[:, :1])

    print("Best KFold Model test MSE:")
    print(kFold_mean_square_error)

    plt.scatter(kFold_test_X,kFold_test_y, label='data')
    plt.plot(kFold_test_X, kFold_preds, color='red')
    plt.legend()
    plt.show()
    
    # Plot comparison
    plt.scatter(test_X, test_y, label='data')
    plt.plot(test_X, lr_preds, label='Linear Regression', color='purple')
    plt.plot(test_X, rd_preds, label='Ridge Regression', color='black')
    plt.plot(test_X, kFold_preds, label='K-fold Ridge Regression', color = "red")
    # plt.legend()
    plt.title('Comparison of Linear and K-fold Ridge Regression')
    plt.show()
    
   
