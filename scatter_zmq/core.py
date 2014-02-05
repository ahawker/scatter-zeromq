"""
    scatter.zmq.core
    ~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'


import zero

from scatter.config import ConfigAttribute
from scatter.service import Service


class Context(zero.Context):
    """
    """



class ZeroService(Service):
    """

    """

    context_class = ConfigAttribute()