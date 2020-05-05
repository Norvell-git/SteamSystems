

class OverSpecififedError(Exception):
    """
    
    """
    print("Raised when too many variables are passed on initialising"
          " the class.")
    pass

class NonSpecifiedError(Exception):
    """
    
    """
    print("No problem could be identified, refer to the documentation and make"
          " sure that a valid combination of parameters is given.")
    pass

class MaxIterationsError(Exception):
    """

    """
    print("The maximum number of iterations has been reached without"
          " converging. Try increaing the max iteraitons or reviewing the" 
          " initial conditions.")
    pass

class InputError(Exception):
    """
    
    """
    print("An expected input is missing.")
    pass

class OutputError(Exception):
    """
    
    """
    print("The calculated value is infeasible.")
    pass
