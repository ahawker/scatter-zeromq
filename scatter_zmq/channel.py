"""
    scatter.channel
"""

__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = 'ChannelService'.split()

#import scatter
#import stream

from scatter.config import ConfigAttribute
from scatter.dependency import DependencyAttribute
from scatter.descriptors import cached
from scatter.protocol import MessageHandler
from scatter.service import Service
from scatter.utils import iterable






#LOG = log.get_log(__name__)

# import zmq.green as zmq
# from scatter import stream
# from scatter import protocol
# from scatter import utils
#
# #channel wraps a socket and allows encode/decode/compression/multiplexing? etc
#
# #channel is multiple publishers and a single subscriber
#
# class Channel(object):
#     def __init__(self, socket_type, ctx=None, codec=None, compress=False):
#         self.protocol = protocol.Protocol(codec, compress)
#         self.stream = stream.Stream(socket_type, ctx)
#         self.stream.recv_callback(self.on_msg_recv)
#
#     # @property
#     # def ctx(self):
#     #     return self.stream.ctx
#
#     # def connect(self, endpoints):
#     #     for endpoint in utils.iterable(endpoints):
#     #         self.stream.connect(endpoint)
#     #
#     # def bind(self, endpoints):
#     #     for endpoint in utils.iterable(endpoints):
#     #         self.stream.bind(endpoint)
#     #
#     # def close(self):
#     #     self.stream.close()
#
#     @staticmethod
#     def on_msg_recv(stream, msg):
#         pass
#
#
# class ChannelMultiplexer(object):
#     pass #hrm - do we need to propagate msgs?



#A channel is the combination of a message handler and one or many streams


#
# class ChannelStateMachine(state.StateMachine):
#     _initial_state = 'init'
#
#     @state.transition('init', 'initialized')
#     def _initializing(self, *args, **kwargs):
#         self.on_initializing(*args, **kwargs)
#
#     @state.transition('initialized', 'open')
#     def _opening(self, *args, **kwargs):
#         self.on_opening(*args, **kwargs)
#
#     @state.transition('open', 'closed')
#     def _closing(self, *args, **kwargs):
#         self.on_closing(*args, **kwargs)
#
#
# class BaseChannel(ChannelStateMachine):
#     _uri = None
#     _name = None
#
#     def __init__(self, opts):
#         super(BaseChannel, self).__init__()
#         self.log = opts.log or LOG
#         self._uri = opts.uri or uri.generate_uri()
#         self._name = opts.name or '{0}:{1}'.format(self.type, self.uri)
#
#     def __enter__(self):
#         self.open()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
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
#     def open(self):
#         self.to('open')
#
#     def close(self):
#         self.to('close')
#
#     def on_initializing(self, *args, **kwargs):
#         self.log.info('[{0}] channel initializing.'.format(self.name))
#
#     def on_opening(self, *args, **kwargs):
#         self.log.info('[{0}] channel opening.'.format(self.name))
#
#     def on_closing(self, *args, **kwargs):
#         self.log.info('[{0}] channel closing.'.format(self.name))
#
#
# class Channel(BaseChannel, stream.StreamPoolMixin):
#
#     def __init__(self, opts):
#         super(Channel, self).__init__(opts)
#
#
# class Channel(BaseChannel, stream.StreamPoolMixin):
#
#     def __init__(self, opts):
#         super(Channel, self).__init__(opts)






class ChannelService(Service):
    """

    """

    #:
    #:
    message_handler_class = ConfigAttribute()

    #:
    #:
    stream_class = ConfigAttribute()

    #:
    message_handler = DependencyAttribute(type='scatter.protocol.MessageHandler')


    @property
    def streams(self):
        return self.services.by_type(self.stream_class).all()

    # def add_stream(self, stream):
    #     # stream.on_recv(self.message_handler.on_recv_callback)
    #     # stream.on_send(self.message_handler.on_send_callback)
    #     # stream.on_close(self.on_close_callback)
    #     self.attach(stream)

    def connect(self):
        """
        """


    def bind(self):
        pass

    # def connect(self, endpoints):
    #     for endpoint in iterable(endpoints):
    #         pass
    #
    # def bind(self, endpoints):
    #     for endpoint in iterable(endpoints):
    #         pass
    #
    # def send(self, msg):
    #     for s in self.streams:
    #         s.send(msg)
    #
    # def recv(self):
    #     pass

    def on_msg_recv(self, stream, msg):
        """

        :param stream:
        :param msg:
        :return:
        """
        self.log.info('Channel recv message! {0} {1}'.format(stream, msg))

    def on_msg_send(self, stream, msg):
        """

        :param stream:
        :param msg:
        :return:
        """
        self.log.info("Channel sent message!")

    def on_recv_stream(self, stream, msg):
        """

        :param stream:
        :param msg:
        :return:
        """
        self.message_hander.on_recv_callback(stream, msg)

    def on_send_stream(self, stream, msg):
        """

        :param stream:
        :param msg:
        :return:
        """
        self.message_handler.on_send_callback(stream, msg)

    def on_close_callback(self, stream):
        """

        :param stream:
        :return:
        """
        self.log.info('{0} closed'.format(stream))

    def on_initialized(self):
        """

        :return:
        """
#        self.config.setdefault('MESSAGE_HANDLER_CLASS', MessageHandler)
#        self.config.setdefault('STREAM_CLASS', Stream)
#        self.dependencies.

    def on_attached(self, parent):
        pass

    # def on_starting(self):
    #     """
    #
    #     :return:
    #     """
    #     pass
    #
    # def on_stopping(self):
    #     """
    #
    #     :return:
    #     """
    #     pass


