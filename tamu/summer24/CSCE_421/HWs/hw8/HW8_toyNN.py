import numpy as np
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

# read_data, get_df_shape, data_split are the same as HW3
def read_data(filename: str) -> pd.DataFrame:
    d = pd.read_csv(filename)
    df = pd.DataFrame(data=d)
    return df

def extract_features_label(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    # Filter the dataframe to include only Setosa and Virginica rows
    filtered_df = df[df['variety'].isin(['Setosa', 'Virginica'])]
    # Extract the required features and labels from the filtered dataframe
    features = filtered_df[['petal.length', 'petal.width']]
    labels = filtered_df['variety'].map({'Setosa': 0, 'Virginica': 1})
    return features, labels

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def function_derivative(z):
    fd = sigmoid(z)
    return fd * (1 - fd)


class NN:
    def __init__(self, features, hidden_neurons, output_neurons, learning_rate):
        self.features = features
        self.hidden_neurons = hidden_neurons
        self.output_neurons = output_neurons
        self.learning_rate = learning_rate
        
        # initialize weights
        self.V = np.random.randn(self.features, self.hidden_neurons)
        self.W = np.random.randn(self.hidden_neurons, self.output_neurons)
        
        # initialize biases: 0
        self.V0 = np.zeros((self.hidden_neurons))
        self.W0 = np.zeros((self.output_neurons))
    
    def train(self, X, t, epochs=1000):
        costs = []
        for epoch in range(epochs):
            # forward pass
            net_u = X.dot(self.V) + self.V0
            H = sigmoid(net_u)
            net_z = H.dot(self.W) + self.W0
            O = sigmoid(net_z)
            
            # backpropagation pass
            error_output = O - t
          
            d_W = H.T.dot(error_output * function_derivative(net_z))
            d_W0 = np.sum(error_output * function_derivative(net_z), axis=0)
           
            error_hidden_layer = error_output.dot(self.W.T) * function_derivative(net_u)
            d_V = X.T.dot(error_hidden_layer)
            d_V0 = np.sum(error_hidden_layer, axis=0)
            
            # update weights and biases
            self.W -= self.learning_rate * d_W
            self.W0 -= self.learning_rate * d_W0
            self.V -= self.learning_rate * d_V
            self.V0 -= self.learning_rate * d_V0
            
            #find the cost function
            if epoch % 10 == 0:
                loss =  np.square(np.subtract(t,O)).mean() 
                costs.append(loss)
                
        return costs
    
    def predict(self, X):
        net_u = X.dot(self.V) + self.V0
        H = sigmoid(net_u)
        net_z = H.dot(self.W) + self.W0
        O = sigmoid(net_z)
     
        return (O > 0.5).astype(int)
    
if __name__ == "__main__":
    def accuracy(t, y_pred):
        accuracy = np.sum(t == y_pred) / len(t)
        return accuracy

    # Read the data
    train_df = read_data("/Users/aduysak03/Desktop/den23/iris_training_data.csv")
    test_df = read_data("/Users/aduysak03/Desktop/den23/iris_testing_data.csv")
    
    X, t =  extract_features_label(train_df)
    X_test, t_test = extract_features_label(test_df)

    t = t.values.reshape([len(t),1])
    t_test = t_test.values.reshape([len(t_test),1])
    
# create Neural Network class
nn = NN(features=2, hidden_neurons=5, output_neurons=1, learning_rate=0.01)

# train the network
cost = nn.train(X, t)

# make predictions on the test data
y_pred = nn.predict(X_test)

# evaluate the accuracy
acc = accuracy(t_test,y_pred)
print(acc)
  
plt.plot(cost)
plt.show()