# Perceptron
## Biological Inspiration
- The **Perceptron** is a simple model of a neuron, mimicking the way a biological neuron works
- Biological neurons:
    - Connected to other neurons through synapses
    - Axons carry signals from the neuron to the synapse
    - Information is only sent between neurons if the signal is strong enough to pass a certain threshold
    - Synapses are modified with learning
- The perceptron was the first algorithmically described neural network
- Mathematically, the perceptron models a neuron as follows:
    - The neuron receives input signals $x_1, x_2, \ldots, x_n$
    - Each input signal is multiplied by a weight $w_1, w_2, \ldots, w_n$
    - The weighted sum of the inputs is calculated: $\sum_{i=1}^{n} w_i x_i = w^T x$
    - The weighted sum is passed through an activation function $f(z)$
    - The output of the neuron is $y = f(z)$
- The weights can be thought of synaptic weights
- The activation function is the threshold to determine if the neuron fires
## Overview
- The perceptron produces continuous output, however it can be easily converted for classification
- The perceptron can be treated as a binary classifier
- However, the perceptron is limited to linearly separable data in the case of binary classification
- With only one neuron, the perceptron can only classify between two classes
- Expanding the output layer to have more than one neuron allows for multi-class classification, still limited to linearly separable data
## Linear Separability
- A set of points is **linearly separable** if there exists a hyperplane that separates the points into two classes
- A linearly separable set of points can be classified by a single layer perceptron
- If a set of points is not linearly separable, a multi-layer perceptron can be used
## Perceptron Architecture
- Has the following:
    - An input vector $x = [x_1, x_2, \ldots, x_n]$
    - A weight vector $w = [w_1, w_2, \ldots, w_n]$
    - A bias term $b$
    - An activation function $f(z)$
    - An output $y = f(w^T x + b)$
- We call the term $w^T x + b$ the **net**, often denoted as $z$
## Activation Functions
- The **rectified linear unit (ReLU)** is a very common activation function
- The ReLU is defined as:
    - $\text{ReLU}(z) = \max(0, z)$
- Additional activation functions include:
    - **Heaviside step function** - $y = \begin{cases} 1 & z \ge 0 \\ 0 & z < 0 \end{cases}$
    - **Logistic sigmoid** - $y = \frac{1}{1 + e^{-z}}$
    - **Hyperbolic tangent** - $y = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$
    - **Soft ReLU** - $y = \log 1 + e^z$
- The **sigmoid** is another very common activation function: $y = \frac{1}{1 + e^{-net}}$