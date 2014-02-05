"""
    scatter.socket
    ~~~~~~~~~~~~~~

    Contains functionality for extending ZeroMQ sockets.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

#import utils
import zero

from scatter.socket import Socket

#import zmq.green as zmq
#from gevent import local
#from scatter import stream
#from scatter import protocol
#from scatter import channel

#add class to patch zmq socket with send_msgpack, recv_msgpack 'helpers'


#
# class Socket(object):
#     def __init__(self, socket_type, ctx=None, loop=None, codec=None):
#         self.stream = stream.Stream(socket_type, ctx, loop)
#         self.stream.on_recv(self.on_recv)
#         self.stream.on_recv_stream(self.on_recv_stream)
#         self.protocol = protocol.Protocol(codec)
#
#     @property
#     def ctx(self):
#         return self.stream.ctx
#
#     def connect(self, endpoints):
#         self.stream.connect(endpoints)
#
#     def bind(self, endpoints):
#         self.stream.bind(endpoints)
#
#     def send(self, msg):
#         self.stream.send(msg)
#
#     def close(self):
#         self.stream.close()
#
#     @staticmethod
#     def on_recv_stream(msg, stream):
#         stream.queue.put(stream.protocol.decode_msg(msg))
#
# class SocketSet(local.local):
#     def __init__(self, **kwargs):
#         kwargs.setdefault('connected', dict())
#         kwargs.setdefault('bound', dict())
#         super(SocketSet, self).__init__(**kwargs)
#
#     def add(self, name, socket_type):
#         pass
#
#     def connect(self, name, socket_type, endpoints):
#         self.connected[name] = (socket_type, endpoints)
#
#     def bind(self, name, socket_type, endpoints):
#         self.bound[name] = (socket_type, endpoints)

# class Request(Socket):
#     def __init__(self, socket_type=zmq.REQ, ctx=None):
#         super(Request, self).__init__(socket_type, ctx)
#
# class Reply(Socket):
#     def __init__(self, socket_type=zmq.REP, ctx=None):
#         super(Reply, self).__init__(socket_type, ctx)
#
# class Router(Socket):
#     def __init__(self, socket_type=zmq.ROUTER, ctx=None):
#         super(Router, self).__init__(socket_type, ctx)
#
# class Dealer(Socket):
#     def __init__(self, socket_type=zmq.DEALER, ctx=None):
#         super(Dealer, self).__init__(socket_type, ctx)
#
# class Push(Socket):
#     def __init__(self, socket_type=zmq.PUSH, ctx=None):
#         super(Push, self).__init__(socket_type, ctx)
#
# class Pull(Socket):
#     def __init__(self, socket_type=zmq.PULL, ctx=None):
#         super(Pull, self).__init__(socket_type, ctx)
#
# class Publisher(Socket):
#     def __init__(self, socket_type=zmq.PUB, ctx=None):
#         super(Publisher, self).__init__(socket_type, ctx)
#
# class Subscriber(Socket):
#     def __init__(self, socket_type=zmq.SUB, ctx=None):
#         super(Subscriber, self).__init__(socket_type, ctx)


# def create_socket(ctx, socket_type, method, endpoints):
#     sock = Socket(ctx, socket_type)
#     for endpoint in utils.iterable(endpoints):
#         getattr(sock, method)(endpoint)
#     return sock
#
#
# class Socket(zero.Socket):
#     def __init__(self, ctx, socket_type, *args, **kwargs):
#         super(Socket, self).__init__(ctx, socket_type, *args, **kwargs)
#
#     @property
#     def synchronous(self):
#         return self.socket_type in (zero.REQ, zero.REP)


class ZeroSocket(Socket):
    """

    """

    @property
    def socket_type(self):
        return self._socket.socket_type

    def connect(self, address):
        """

        :param address:
        :return:
        """
        return self._socket.connect(address)

    def bind(self, address):
        """

        :param address:
        :return:
        """
        return self._socket.bind(address)

    def send(self, msg):
        """

        :param msg:
        :return:
        """
        return self._socket.send_multipart(msg)

    def recv(self):
        """

        :return:
        """
        return self._socket.recv_multipart()

    def close(self):
        """

        :return:
        """
        return self._socket.close()

