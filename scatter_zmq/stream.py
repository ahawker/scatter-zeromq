"""
    scatter.stream
    ~~~~~~~~~~~~~~

    ...
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = 'Stream StreamService'.split()

#import async
#import codecs
#import config
#import descriptors
#import log
#import service
#import socket
#import state
#import protocol
#import uid
#import zero

import functools
import zero

from scatter.codec import Codec
from scatter.config import ConfigAttribute
from scatter.descriptors import cached
from scatter.service import Service
#from scatter.stream import Stream

#LOG = log.get_log(__name__)
#
#
# # def create_stream(ctx, socket_type, method, endpoints, ioloop):
# #     sock = socket.create_socket(ctx, socket_type, method, endpoints)
# #     return Stream(sock, ioloop)
#
#
# # class StreamPoolMixin(TypedAsyncPoolMixin):
# #     _supported_types = None
# #
# #     @property
# #     def streams(self):
# #         return self._items
#
#
# # class StreamPoolMixin(object):
# #     _streams = async.pool()
# #
# #     def __iter__(self):
# #         return iter(self.streams)
# #
# #     @property
# #     def streams(self):
# #         return self._streams
# #
# #     def add_stream(self, stream):
# #         self.streams.add(stream)
# #
# #     def on_opening(self, *args, **kwargs):
# #         for stream in (s for s in self.streams if s.is_state('initialized')):
# #             stream.open(*args, **kwargs)
# #
# #     def on_closing(self, *args, **kwargs):
# #         for stream in (s for s in self.streams if s.is_state('open')):
# #             stream.close(*args, **kwargs)
# #
# #
# class StreamStateMachine(state.StateMachine):
#
#     def __init__(self):
#         super(StreamStateMachine, self).__init__('open')
#
#     @state.transition('open', 'closed')
#     def _closing(self, *args, **kwargs):
#         self.on_closing(*args, **kwargs)
#
#
# class BaseStream(StreamStateMachine):
#     _uri = None
#     _name = None
#
#     def __init__(self, *args, **kwargs):
#         super(BaseStream, self).__init__()
#         self.log = kwargs.get('log') or LOG
#         self._uri = kwargs.get('uri') or uri.generate_uri()
#         self._name = kwargs.get('name') or '{0}:{1}'.format(self.type, self.uri)
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def type(self):
#         return self.__class__.__name__
#
#     @property
#     def uri(self):
#         return self._uri
#
#     def close(self, *args, **kwargs):
#         self.to_state('close', *args, **kwargs)
#
#     def on_closing(self, *args, **kwargs):
#         self.log.info('[{0}] stream closing.'.format(self.name))
#
#
# # class Stream(zero.Stream):
# #
# #     def __init__(self, socket, ioloop, log=None):
# #         super(Stream, self).__init__(socket, ioloop)
# #         self.log = log or LOG
# #
# #     def close(self):
# #         pass
#
# class Stream(BaseStream):
#     _stream = None
#
#     def __init__(self, socket, ioloop, *args, **kwargs):
#         kwargs.setdefault('log', LOG)
#         super(Stream, self).__init__(*args, **kwargs)
#         self._stream = zero.Stream(socket, ioloop)
#
#     @property
#     def stream(self):
#         return self._stream
#
#     @property
#     def type(self):
#         return self._stream.socket_type
#
#     def on_recv_stream(self, callback):
#         return self.stream.on_recv_stream(callback)
#
#     def on_send_stream(self, callback):
#         return self.stream.on_send_stream(callback)
#
#     def on_closing(self, *args, **kwargs):
#         pass #kill cb's, close stream +socket, must be in ioloop cb ctx tho

#
# class Stream(service.BaseService):
#     _stream = None
#
#     def __init__(self, socket, ioloop, *args, **kwargs):
#         super(Stream, self).__init__(*args, **kwargs)
#         self._stream = zero.Stream(socket, ioloop)
#         self.on_recv_stream = self.stream.on_recv_stream
#         self.on_send_stream = self.stream.on_send_stream
#
#     @property
#     def stream(self):
#         return self._stream
#
#     @property
#     def stream_type(self):
#         return self.stream.socket_type
#
#     def on_stopping(self, *args, **kwargs):
#         pass


# class ZStream(zero.Stream):
#     """
#
#     """


class Socket(zero.Socket):
    """

    """


class Stream(zero.Stream):
    """
    """

    def on_send(self, func):
        """
        """
        callback = self.callback(func)
        super(Stream, self).on_send(callback)

    def on_recv(self, func):
        """
        """
        callback = self.callback(func)
        super(Stream, self).on_recv(callback)

    def on_close(self, func):
        """
        """
        callback = self.callback(func)
        super(Stream, self).set_close_callback(callback)

    def callback(self, func):
        """
        Wrap the given callback function to contain the Stream object which raised the callback
        as the first argument.

        :param func: Callback to raise.
        """
        if not callable(func):
            raise ValueError('Callback must be a callable')

        @functools.wraps(func)
        def cb(*args, **kwargs):
            return func(self, *args, **kwargs)
        return cb


class StreamService(Service):
    """

    """

    #:
    #:
    codec_class = ConfigAttribute()

    #:
    #:
    stream_class = ConfigAttribute()

    #:
    #:
    socket_class = ConfigAttribute()

    #:
    #;
    socket_type = ConfigAttribute()

    @classmethod
    def req(cls):
        return cls(config=dict(socket_type=zero.REQ))


    def send(self, msg):
        pass

    def recv(self, msg):
        pass

    def create_stream(self, parent):
        """

        :param parent:
        :return:
        """
#        s = Socket(zero.REQ, parent.context)
#        return Stream(s, parent.ioloop)

    def on_initializing(self):
        """

        :param parent:
        :param conf:
        :return:
        """
        self.config.setdefault('CODEC_CLASS', Codec)
        self.config.setdefault('STREAM_CLASS', Stream)
        self.config.setdefault('SOCKET_CLASS', Socket)
        self.config.setdefault('SOCKET_TYPE', None)

    def on_started(self):
        """

        :return:
        """
        pass
        #self.stream = create_stream(self.socket_type)

    def on_stopping(self):
        """

        :return:
        """
        events = self.stream.flush()
        self.log.info('Closing stream after {0} events flushed'.format(events))
        self.stream.close()

    def on_attached(self, parent):
        """

        :param parent:
        :return:
        """
        # self.stream = self.create_stream(parent)
        # self.stream.on_recv_stream(parent.on_recv_stream)
        # self.stream.on_send_stream(parent.on_send_stream)
        # self.stream.on_close_stream(parent.on_close_stream)
