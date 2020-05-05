

class OverSpecififedError(Exception):
    """
    Raised when too many variables are passed on initialising the class.
    """
    pass

class NonSpecifiedError(Exception):
    """
    No problem could be identified, refer to the documentation and make
    sure that a valid combination of parameters is given.
    """
    pass

class MaxIterationsError(Exception):
    """
    The maximum number of iterations has been reached without converging.
    Try increaing the max iteraitons or reviewing the initial conditions.
    """
    pass

class InputError(Exception):
    """
    An expected input is missing
    """

class OutputError(Exception):
    """
    The calculated value is infeasible.
    """