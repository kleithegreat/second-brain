# Neural Networks
- One of the most effective general-purpose supervised learning algorithms
- They can approximate any function given one hidden layer and a sufficient number of neurons
- A **multi-layer perceptron** is a neural network with one or more hidden layers
    - An *n* layer neural network is a network with *n-1* hidden layers
    - Inputs are not counted as layers generally
- The capacity of a neural network grows with the number of hidden layers and the number of neurons in each layer
- It has been mathematically proven that a neural network with one hidden layer can approximate any function given a sufficient number of neurons
- The MLP has two main components:
    - A **forward pass** that performs inference
    - A **backward pass** that learns
- In training, we want to find the weights that minimize the loss function
$$ w^* = \arg\min_w \sum_{n=1}^N \text{loss}(o^n, t^n) $$
- Where $o^n$ is the output of the network for input $x^n$ and $t^n$ is the target output and $o = f(x, w)$
- Two common loss functions are **squared loss** and **cross-entropy loss**
    - Squared loss: $\sum_k \frac{1}{2} (o^n_k - t^n_k)^2$
    - Cross-entropy loss: $-\sum_k t^n_k \log(o^n_k)$
- The most commonly used activation functions are sigmoid, tanh, and ReLU
## Backpropagation
- An efficient method for computing gradients
- Training:
```
Loop until convergence:
    For each example n
        given input x^n, compute the output o^n (forward pass)
        propagate gradients backward (backward pass)
        update weights
```
- The key idea behind backpropagation is that we dont have targets for a hidden unit
    - Use error derivatives with respect to hidden units
    - Since one hidden unit can affect multiple output units, we need to use the chain rule