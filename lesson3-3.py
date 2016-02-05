import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced
    # predictions.
    #
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    sum_of_square_errors = np.square(data - predictions ).sum()
    sum_of_square_mean = np.square(data - np.mean(data) ).sum()
    r_squared = 1.0 - (sum_of_square_errors/sum_of_square_mean)
    return r_squared