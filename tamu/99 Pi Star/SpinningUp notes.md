# **Spinning Up**

## **Part 1: Key Concepts in RL**

- Two main characters in RL: **agent** and **environment**
- Agent-Environment action loop:
    - The agent observes the environment
        - This could either be a whole or partial observation
    - The agent decides on an action depnding on its observation
    - The environment changes based on the agents action
        - The environment can also change on its own
- The agent is given a **reward** from the environment for each action it takes
    - The reward describes how good or bad the current environment is
- The goal of RL is the maximize reward
    - This is called the **return**

### **States and Observations**
- A **state** is the complete description of the environment
    - An *observation** is a partial description of a state
- Agents can either **fully observe** or **partially observe** an environment

> Somtimes in RL, states and observations are used interchangably (although inaccurately)

### **Action Spaces**
- An action space is the set of all valid actions for a given environment
    - Action spaces can be either discrete or continuous
    - Discrete action spaces have a finite number of actions
    - Continuous action spaces can be represented with real valued vectors
- Different RL algorithms may need different implementations depending if an environments action space is discrete or continuous

### **Policies**
- A **policy** is what an agent uses to determine what action to take
- Policies can be either **deterministic** or **stochastic**
    - Deterministic policies always determine the same action for a particular state
    - Stochastic policies give a probability distribution over a set of possible actions
- Deep RL deals with **parameterized policies**
    - These are policies that use a function of parameters to determine what action to take
        - This function can be optimized
    - The parameters of parameterized policy are often denoted by theta or phi

#### **Stochastic Policies**
- Two most common kinds: **categorical** and **diagonal gaussian**
    - Categorical -> discrete action space
    - Gaussian -> continuous
- A **categorical policy** is like a classifier over discrete actions
    - Input is the observation, output uses a softmax to convert final layer into probabilities
- A **diagonal gaussian policy** samples the action from a **diagonal gaussian distribution**
    > Context:
    >    - A **multivariate gaussian distribution** (gaussian = normal) generalizes one dimensional normal distributions to multiple dimensions
    >       - The **mean vector** has elements that are averages of each dimension of the distribution
    >       - The **covariance matrix** is a square matrix whose length and width are the variables of a dataset. The ith and jth entry represents the covariances between the ith and jth variables. The covariance of the same variable is the variance.
    >    - A **diagonal gaussian distribution** is a special multivariate gaussian distribution where its covariance matrix only has entreis on the diagonal
    >       - As a result, its covariance matrix can be represented with just a vector
    - diagonal gaussian policies always use a neural network that maps observations to mean actions

### **Trajectories**

### **Reward and Return**

### **The RL Problem**

### **Value Functions**

### **The Optimal Q-Function and Optimal Action**

### **Bellman Equations**

### **Advantage Functions**


## **Part 2: Kinds of RL Algorithms**


## **Part 3: Intro to Policy Optimization**

