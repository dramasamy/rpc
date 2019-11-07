#!/usr/bin/env python
import socket, signal
from SimpleXMLRPCServer import *

class AltXMLRPCServer(SimpleXMLRPCServer):

    finished=False

    def register_signal(self, signum):
        signal.signal(signum, self.signal_handler)

    def signal_handler(self, signum, frame):
        print "Caught signal", signum
        self.shutdown()

    def shutdown(self):
        self.finished=True
        return 1

    def serve_forever(self):
        while not self.finished: server.handle_request()


class MyFuncs:
    def div(self, x, y) :
        """Returns division of two numbers"""
        return x // y

    def add(self, x, y) : return x + y


hostname=socket.gethostname(); port=8086
server = AltXMLRPCServer((hostname, port))
print "Serving on %s:%d" %(hostname, port)
server.register_function(pow)
server.register_function(server.shutdown)
server.register_function(lambda x,y: x-y, 'minus')
server.register_introspection_functions()
server.register_instance(MyFuncs())
server.register_signal(signal.SIGHUP)
server.register_signal(signal.SIGINT)

server.serve_forever()
print "Closed"
