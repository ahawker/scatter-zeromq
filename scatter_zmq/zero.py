"""
    scatter.zero
    ~~~~~~~~~~~~

    Contains functionality for interacting with ZeroMQ.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

from zmq import green as zmq
from zmq.green.eventloop import ioloop as ioloop
from zmq.green.eventloop import zmqstream as zmqstream


Context = zmq.Context
Socket = zmq.Socket

REQ = zmq.REQ
REP = zmq.REP

Stream = zmqstream.ZMQStream
IOLoop = ioloop.IOLoop
PeriodicCallback = ioloop.PeriodicCallback
DelayedCallback = ioloop.DelayedCallback
