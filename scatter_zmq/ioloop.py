"""
    scatter_zmq.ioloop
    ~~~~~~~~~~~~~~~~~~

    ...
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = 'IOLoopService'.split()

import functools
import zero


from scatter.async import AsyncService
from scatter.config import ConfigAttribute
from scatter.descriptors import cached
from scatter.service import Service



class IOLoop(zero.IOLoop):
    """

    """

    @staticmethod
    def instance():
        if not IOLoop.initialized():
            with IOLoop._instance_lock:
                if not IOLoop.initialized():
                    IOLoop._instance = IOLoop()
        return IOLoop._instance

    @staticmethod
    def current():
        current = getattr(IOLoop._current, 'instance', None)
        if current is not None:
            return current
        return IOLoop.instance()

    @staticmethod
    def initialized():
        return hasattr(IOLoop, '_instance')

    def add_periodic_callback(self, callback, interval, *args, **kwargs):
        callback = functools.partial(callback, *args, **kwargs)
        cb = zero.PeriodicCallback(callback, interval, self)
        cb.start()

    def add_delayed_callback(self, callback, delay, *args, **kwargs):
        callback = functools.partial(callback, *args, **kwargs)
        cb = zero.DelayedCallback(callback, delay, self)
        cb.start()

    def run(self):
        self.start()
        self.close()



#@depends('scatter.async.async')
class IOLoopService(Service):
    """

    """

    #:
    #:
    ioloop_class = ConfigAttribute(IOLoop)

    #:
    #:
    ioloop_stop_timeout = ConfigAttribute(5)

    #:
    #:
    context_class = ConfigAttribute(zero.Context)


    @cached
    def context(self):
        return self.context_class.instance()

    @cached
    def ioloop(self):
        """
        """
        return self.ioloop_class.current()

    def on_started(self):
        """
        """
        self.worker = self.greenlets.spawn(self.ioloop.run)

    def on_stopping(self):
        """
        """
        self.ioloop.add_callback(self.ioloop.stop)

        self.worker.join(self.ioloop_stop_timeout)
        if self.worker.running():
           self.log.warning('IOLoop worker {0} failed to stop.'.format(self.worker))
