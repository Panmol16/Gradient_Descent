# Gradient_Descent
A program that solves a simple linear regression problem with the gradient descent optimization algorithm

# Depenedencies 

1) numpy
2) pandas
3) matplotlib

# What is Gradient Descent?

Well gradient descent is an optimization algorithm that uses the negative derivative of a function to find it's local minimum. More on gradient descent [here](https://en.wikipedia.org/wiki/Gradient_descent).

# How does it work?

Well we are using Gradient Descent to minimise the value of our cost function which tells us how efficient our model for predicting the data is. In this program, I am use the MSE - [Mean Squared Error](https://en.wikipedia.org/wiki/Mean_squared_error) as my cost function. The MSE is defined as:

![MSE](https://i.stack.imgur.com/19Cmk.gif)

# Minimizing the MSE

To minimize the MSE, we take it's partial derivative with respect to the input parameters. Since we are in linear regression, we only have two things to worry about - **Slope** and the **Intercept**

The derivative are:

![Derivatives](https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png)

Where m is the slope and b is your intercept.

# Running the code

To run the code, all you really need to do is type `python linear_regression.py` and it should work if you have installed all the dependencies.

You can change your input data file from data.csv to data1.csv for a change.

# Data1.csv

The data1.csv file has been created from the [Desmos](https://www.desmos.com/) linear regression example [here](https://www.desmos.com/calculator/jwquvmikhr). 

See if you can train the model with the right learning rate and iterations so as to match the values desmos shows!
