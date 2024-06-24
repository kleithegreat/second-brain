from collections import Counter
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def entropy(x):
    '''
    Calculate the entropy of a list of values.
    Args:
        x: list of values
    Returns:
        float: entropy of the values
    '''
    _, counts = np.unique(x, return_counts=True)
    probabilities = counts / len(x)
    return -np.sum(probabilities * np.log2(probabilities))

def accuracy(y_true, y_pred):
        '''
        Calculate the accuracy of the predicted values.
        Args:
            y_true: list of true values
            y_pred: list of predicted values
        Returns:
            float: average accuracy of the predicted values
        '''
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

class Node:
    def __init__(
        self, feature=None, threshold=None, left=None, right=None, *, value=None
    ):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.value is not None


class TreeRegressor:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.root = self.build_tree(X, y)

    def predict(self, X):
        return np.array([self.traverse_tree(x, self.root) for x in X])

    def build_tree(self, X, y, depth=0):
        '''
        Build the decision tree using a recursive algorithm.
        Args:
            X: list of features
            y: list of labels
            depth: current depth of the tree
        Returns:
            Node: root node of the decision tree

        '''
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            leaf_value = self.common_thing(y)
            return Node(value=leaf_value)
        
        n_feat = n_features if self.n_features is None else min(self.n_features, n_features)
        feat_idxs = np.random.choice(n_features, n_feat, replace=False)
        best_feat, best_thresh = self.get_best_split(X, y, feat_idxs)
        left_idxs, right_idxs = self.split(X[:, best_feat], best_thresh)

        left = self.build_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self.build_tree(X[right_idxs, :], y[right_idxs], depth+1)
        return Node(best_feat, best_thresh, left, right)

    def get_best_split(self, X, y, feat_idxs):
        '''
        Find the best feature and threshold to split the data.
        Args:
            X: list of features
            y: list of labels
            feat_idxs: list of feature indices
        Returns:
            tuple: index of the best feature and the best threshold
        '''
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self.information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold

        return split_idx, split_thresh

    def information_gain(self, y, X_column, split_thresh):
        '''
        Calculate the information gain from a split.
        Args:
            y: list of labels
            X_column: list of values
            split_thresh: threshold to split the values
        Returns:
            float: information gain from the split
        '''
        parent_entropy = entropy(y)

        left_idxs, right_idxs = self.split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        return parent_entropy - child_entropy


    def split(self, X_column, split_thresh):
        '''
        Split the values in X_column based on the split threshold.
        Args:
            X_column: list of values
            split_thresh: threshold to split the values
        Returns:
            tuple: indices of the values that are less than the threshold and indices of the values that are greater than the threshold
        '''
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def traverse_tree(self, x, node):
        '''
        Traverse the tree to find the value of a leaf node.
        Args:
            x: list of features
            node: current node in the tree
        Returns:
            value of the leaf node
        '''
        if node.is_leaf():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self.traverse_tree(x, node.left)
        
        return self.traverse_tree(x, node.right)

    def common_thing(self, y):
        '''
        Find the most common thing in a list of values.
        Args:
            y: list of values
        Returns:
            most common value in the list
        '''
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        return most_common
    

    
if __name__ == "__main__":
    # Load the data
    filename = "./car.data"
    column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
    data = pd.read_csv(filename, header=None, names=column_names)

    # Convert categorical variables to numerical
    for col in data.columns:
        data[col] = data[col].astype('category').cat.codes

    X = data.drop('class', axis=1).values
    y = data['class'].values
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
  
    accuracy_depths = []
    for depth in range(1, 6):   
        clf = TreeRegressor(max_depth=depth)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy(y_test, y_pred)
        accuracy_depths.append(acc)
        print("Accuracy at depth %d: %f" % (depth, acc))
        

    plt.plot(range(1, 6), accuracy_depths)
    plt.xlabel("Depth")
    plt.ylabel("Accuracy")
    plt.title("Decision Tree Accuracy by Depth")
    plt.show()


    #Using sklearn DecisionTreeClassifier only to compare and visualilze the tree
    sklearn_clf = DecisionTreeClassifier(max_depth=depth)
    sklearn_clf.fit(X_train, y_train)
    sklearn_y_pred = sklearn_clf.predict(X_test)
    # Plot the tree
    plt.figure(figsize=(20,10))
    plot_tree(sklearn_clf, feature_names=column_names[:-1], class_names=sklearn_clf.classes_.astype(str), filled=True)
    plt.title("Visualization of Decision Tree Structure using sklearn Classifier")
    plt.show()