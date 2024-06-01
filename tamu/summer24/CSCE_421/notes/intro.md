# Introduction to Machine Learning
- **Machine Learning** is a subfield of artificial intelligence that focuses on the development of algorithms that allow computers to learn from and make predictions or decisions based on data
- **Artificial Intelligence** can be defined as the capability of a machine to *imitate intelligent human behavior*
- AI and ML are oftentimes used interchangeably, but they are not the same thing, and ML is a subset of AI
    - AI is the general idea of machines being able to carry out tasks in a way that we would consider "smart"
    - ML refers to the technologies that allow machines to:
        - identify patterns in data
        - make decisions based on those patterns
        - improve their performance over time
- "GOFAI" (Good Old-Fashioned Artificial Intelligence) is the traditional approach to AI, which involves writing rules and algorithms to solve problems
    - This approach is limited because it requires a lot of human effort to write the rules
    - It is difficult to write rules for every possible situation
    - This is an example of AI that is not ML
- **Deep Learning** is a subset of ML that uses neural networks with many layers to learn from data
    - Deep learning is a subset of ML, which is a subset of AI
- AI consists of tools like:
    - ML
    - DL
    - Neural Networks
    - Computer vision
    - Natural Language Processing
- "Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed." - Arthur Samuel
- ML can be used in some useful tasks like:
    - Detecting objects in images
    - Speech recognition
    - Knowledge discovery in the medical field
    - Predictive analytics (e.g. predicting stock prices)
- Another definition of ML:
    - A program **M** is said to *learn*
    - from experience **E**
    - with respect to some class of tasks **T**
    - and performance measure **P**
    - if its performance as measured by **P** on tasks in **T** in an environment **Z** improves with experience **E**
- Example:
    - **T** - cancer detection
    - **E** - set of diagnostic cases
    - **P** - percentage of cases correctly diagnosed
    - **Z** - noisy measurements, occasional errors in diagnosis
    - **M** - a program that runs on a general-purpose computer
## Why bother with machine learning?
1. The structure of the task is not well understood, but representative data is available
2. Task parameters vary
    - detecting spam
    - recommendation algorithms
    - predicting treatment outcomes
3. Explicitly specifying the knowdledge required to solve a problem is difficult (e.g. handwriting recognition)
4. The task is beyond human capabilities
5. ML can help us understand the structure of the data
### ML is used when:
- Human expertise does not exist
- Human expertise is difficult to formalize
- Models must be customized (e.g. personalized medicine)
- Models are based on huge amounts of data (e.g. genome sequencing)
## Supervised Learning
- **Supervised Learning** is a type of ML where the model is trained on a labeled dataset
    - The model learns to map inputs to outputs
    - The model is trained on a dataset that contains both the input and the correct output
    - The model is then tested on a new dataset to evaluate its performance
- Two main types of supervised learning:
    - **Regression**: the output is a continuous value
    - **Classification**: the output is a category
### Cats vs. Dogs
- Children don't learn the difference between cats and dogs by memorizing a scientific definition
- Rather, they learn by example
- They are shown pictures of cats and dogs and are told which is which
- This would be an example of a supervised classification task
