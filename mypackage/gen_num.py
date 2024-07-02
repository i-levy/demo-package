import numpy as np

def a_number(min=1, max=100):
    """
    Used for generating a random number within a specified range
    
    Inputs
    -------
    min    Minimum value of range, integer, defaults to 1 if nothing specified
    max    Maximum value of range, integer, defaults to 100 if nothing specified
    
    Returns
    -------
    val    A random integer within specified range of values
    """
    
    val = np.random.randint(min, max)
    print(val)