"""
When passed a list of variables from turbine class this will filter out any
over/underspecified problems.
"""

from .functions import (OverSpecififedError, NonSpecifiedError)

def non_specd(vars):
    """
    list formatted as list of booleans whether parameter has been passed
    as an argument. In order of:
    [m_act, Q, W, m_max, m_rat]

    e.g.
    [True, False, False, True, False]
    """

    l1 = vars[0] + vars[1] + vars[2]

    if l1 == 0:
        raise NonSpecifiedError()

    if l1 >= 2:
        print("1")
        raise OverSpecififedError()

    l2 = vars[3] + vars[4]

    if l2 >= 2:
        print("2")
        raise OverSpecififedError()
