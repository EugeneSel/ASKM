import numpy as np


def function(x1, x2):
    return x1 ** 2 + 16 * x2 ** 2


def examining_search(x_basis, delta_x):
    x_current_basis = x_basis
    if function(x_current_basis[0] + delta_x[0], x_current_basis[1]) < function(x_current_basis[0], x_current_basis[1]):
        x_current_basis[0] += delta_x[0]
    elif function(x_current_basis[0] - delta_x[0], x_current_basis[1]) < function(x_current_basis[0], x_current_basis[1]):
        x_current_basis[0] -= delta_x[0]

    if function(x_current_basis[0], x_current_basis[1] + delta_x[1]) < function(x_current_basis[0], x_current_basis[1]):
        x_current_basis[1] += delta_x[1]
    elif function(x_current_basis[0], x_current_basis[1] - delta_x[1]) < function(x_current_basis[0], x_current_basis[1]):
        x_current_basis[1] -= delta_x[1]
    return x_current_basis


def hooke_jeeves(x0, delta_x, epsilon, alpha):
    x_basis = x0
    new_delta_x = delta_x
    x_current_basis = examining_search(x_basis, new_delta_x)
    print("\nBasis point: ", x_basis, "\nCurrent basis point: ", x_current_basis)
    x_current_basis_new = x_current_basis
    x_current_basis = x_basis

    while 1:
        if function(x_current_basis[0], x_current_basis[1]) > function(x_current_basis_new[0], x_current_basis_new[1]):
            x_basis = x_current_basis
            x_current_basis = x_current_basis_new
            print("\nBasis point: ", x_basis, "\nCurrent basis point: ", x_current_basis)
        else:
            if np.linalg.norm(new_delta_x) < epsilon:
                break
            else:
                new_delta_x /= alpha
                x_current_basis = examining_search(x_basis, new_delta_x)

        x_working = 2 * x_current_basis - x_basis
        x_current_basis_new = examining_search(x_working, new_delta_x)

    print("\nBasis point: ", x_basis, "\nCurrent basis point: ", np.round(x_current_basis, 3))

    return np.round(x_current_basis, 3)