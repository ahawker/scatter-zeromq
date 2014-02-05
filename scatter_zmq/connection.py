"""
    scatter.connection
    ~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'


#connection is an encapsulation of the following:
#a channel
#an actor which is being exposed

#the worker or actor host maintains a collection of connections?

#a connection hooks the worker to the actor?-...

#a = Actor('inproc://...', 'type', 'type args')
#a.bind('inproc....')
#c = Connection('inproc://*:1234', actor)


class Connection(object):
    def __init__(self, actor, endpoints):
        self.actor = actor
        self.actor.connect(endpoints)

    def close(self):
        self.actor.close()

