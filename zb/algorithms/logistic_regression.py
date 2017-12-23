# -*- coding: utf-8 -*-
"""
——————————————————————————————————————————————————————————————————————————————————————
Logistic Regression
——————————————————————————————————————————————————————————————————————————————————————
"""

import numpy as np
import matplotlib.pyplot as plt
# import self-defined functions
from zb.algorithms.functions import sigmoid


# step 1. initialize parameters with zeros

def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.

    Argument:
    dim     size of the w vector we want (or number of parameters in this case)

    Returns:
    w       initialized vector of shape (dim, 1)
    b       initialized scalar (corresponds to the bias)
    """
    w = np.zeros(dim, 1)
    b = 0
    return w, b


# step 2. compute the cost function and its gradient

def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation

    Arguments:
    w       weights, a numpy array of size (dim, 1)
    b       bias, a scalar
    X       data of size (dim, number of examples)
    Y       true "label" vector of size (1, number of examples)

    Return:
    cost    negative log-likelihood cost for logistic regression
    dw      gradient of the loss with respect to w, thus same shape as w
    db      gradient of the loss with respect to b, thus same shape as b

    """
    m = X.shape[1]
    A = sigmoid(np.dot(w.T, X) + b)
    cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    # BACKWARD PROPAGATION (TO FIND GRAD)
    dw = 1.0 / m * np.dot(X, (A - Y).T)
    db = 1.0 / m * np.sum(A - Y)

    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())

    grads = {"dw": dw,
             "db": db}

    return grads, cost


# step 3. update parameters with gradient descending (train LR model)

def LR_train(w, b, X, Y, num_iterations, learning_rate, print_cost=True):
    """
    This function optimizes w and b by running a gradient descent algorithm

    Arguments:
    w       weights, a numpy array of size (dim, 1)
    b       bias, a scalar
    X       data of shape (dim, number of examples)
    Y       true "label" vector, of shape (1, number of examples)
    num_iterations      number of iterations of the optimization loop
    learning_rate       learning rate of the gradient descent update rule
    print_cost          True to print the loss every 100 steps

    Returns:
    params      dictionary containing the weights w and bias b
    grads       dictionary containing the gradients of the weights and bias with respect to the cost function
    costs       list of all the costs computed during the optimization, this will be used to plot the learning curve.
    """

    costs = []

    for i in range(num_iterations):

        # Cost and gradient calculation
        grads, cost = propagate(w, b, X, Y)

        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]

        # update rule
        w = w - learning_rate * dw
        b = b - learning_rate * db

        # Record the costs
        if i % 100 == 0:
            costs.append(cost)

        # Print the cost every 100 training examples
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    params = {"w": w,
              "b": b}

    grads = {"dw": dw,
             "db": db}

    return params, grads, costs


# step 4. use trained model to predict

def LR_predict(w, b, X):
    """
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)

    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    """

    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        if A[0, i] > 0.5:
            Y_prediction[0, i] = 1.0
        else:
            Y_prediction[0, i] = 0.0

    assert (Y_prediction.shape == (1, m))

    return Y_prediction


# final: merge all into a model

def model(X_train, Y_train, X_test, Y_test, num_iterations=2000,
          learning_rate=0.5, print_cost=True):
    """
    Builds the logistic regression model by calling the function
    implemented above

    Arguments:
    X_train     training set represented by a numpy array of shape (dim, m_train)
    Y_train     training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test      test set represented by a numpy array of shape (dim, m_test)
    Y_test      test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations  hyperparameter representing the number of iterations to optimize the parameters
    learning_rate   hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost      Set to true to print the cost every 100 iterations

    Returns:
    d -- dictionary containing information about the model.
    """
    print('X_train shape:', X_train.shape)

    # initialize parameters with zeros
    w, b = initialize_with_zeros(X_train.shape[0])

    print('w shape:', w.shape)
    # Gradient descent
    parameters, grads, costs = LR_train(w, b, X_train, Y_train, num_iterations,
                                        learning_rate, print_cost)

    # Retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"]

    print('w shape params:', w.shape)

    Y_prediction_test = LR_predict(w, b, X_test)
    Y_prediction_train = LR_predict(w, b, X_train)

    # Print train/test Errors
    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}

    return d


def plot_lc(d):
    """plot learning curve

    Arguments:
    d       Returned by model function. Dictionary containing information about the model.
    """
    costs = np.squeeze(d['costs'])
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(d["learning_rate"]))
    plt.show()
