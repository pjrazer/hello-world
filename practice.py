import numpy as np

def secant(fun, ini_guess, err_max=1e-6, iter_max=100):
    # Input validation
    if not callable(fun):
        raise ValueError('The first input must be a callable function.')
    if not (isinstance(ini_guess, float) or isinstance(ini_guess, int)):
        raise ValueError('The second input must be a numeric value.')

    # Initialize the second initial guess using a small offset
    h = 1
    x0 = ini_guess
    x1 = ini_guess + h

    # Initialize iteration counter and error
    numIter = 0
    err = abs(x1 - x0)

    # Main loop for the secant method
    while err >= err_max and numIter < iter_max:
        try:
            f0 = fun(x0)
            f1 = fun(x1)

            # Check if the denominator is too small (avoid division by zero)
            if abs(f1 - f0) < 1e-12:
                raise ZeroDivisionError("Denominator too small")

            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            err = abs(x2 - x1)

            # Update values for the next iteration
            x0 = x1
            x1 = x2
            numIter += 1

            if np.isnan(fun(x2)) or np.isinf(fun(x2)):
                return x2, err, numIter, -2

        except (ZeroDivisionError, ValueError, TypeError):
            # Handle exceptions due to invalid function values or division by zero
            return None, None, numIter, -2

    # Check if the algorithm terminated normally or due to max iterations
    if err < err_max:
        return x2, err, numIter, 1
    else:
        return x2, err, numIter, 0
