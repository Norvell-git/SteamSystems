"""
__init__ file for functions
"""

from .simplespec import simple

from .heatspec import heatspec

from .workspec import workspec

from .spec_exceptions import non_specd

from .base import f_abc
from .base import f_dh_IS
from .base import f_n
from .base import f_Wint
from .base import f_W
from .base import f_h_2

from .errors import OverSpecififedError
from .errors import NonSpecifiedError
from .errors import MaxIterationsError
from .errors import InputError
from .errors import OutputError
