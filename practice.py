import numpy as np

def secant(fun, ini_guess, err_max=1e-6, iter_max=100):
    # Initialize the second initial guess using a small offset
    h = 1
    x0 = ini_guess
    x1 = ini_guess + h

    # Initialize iteration counter and error
    numIter = 0
    err = abs(x1 - x0)
    if (not isinstance(err_max, float) and not isinstance(err_max, int)) or err_max<=0:
        raise Exception('The fourth and fifth inputs must be positive scalar values.')
        
    if (not isinstance(iter_max, float) and not isinstance(iter_max, int)) or iter_max<=0:
        raise Exception('The fourth and fifth inputs must be positive scalar values.')
        
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
                
                return x2,err, numIter, -2
                

        except (ZeroDivisionError, ValueError, TypeError):
            # Handle exceptions due to invalid function values or division by zero
            return None, None, numIter, -2

    # Check if the algorithm terminated normally or due to max iterations
    if err < err_max:
        return x2, err, numIter, 1
    else:
        return x2, err, numIter, 0
