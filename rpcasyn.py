import SocketServer
from SimpleXMLRPCServer import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler
import time
 
# Threaded mix-in
class AsyncXMLRPCServer(SocketServer.ThreadingMixIn,SimpleXMLRPCServer): pass
 
# Example class to be published
class TestObject:
    def sleep(self, val):
        time.sleep(val)
        return 1
 
    def add(self, x, y) :
        return x + y
 
    def divide(self, x, y):
        return float(x) / float(y)
 
 
# Instantiate and bind to localhost:8080
server = AsyncXMLRPCServer(('', 8000), SimpleXMLRPCRequestHandler)
 
# Register example object instance
server.register_instance(TestObject())
 
# run!
server.serve_forever()
