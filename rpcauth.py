#!/usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from base64 import b64decode
#import psutil

# The GET function

def get():
    #return psutil.cpu_percent(interval=1, percpu=True)
    return 1


# Server definition

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

    def authenticate(self, headers):
        auth = headers.get('Authorization') 
        try:
            (basic, _, encoded) = headers.get('Authorization').partition(' ')
        except:
            print "No Auth"
            # Client did not ask for authentication
            return 1        
        else:
            print "Auth"
            # Client authentication
            (basic, _, encoded) = headers.get('Authorization').partition(' ')
            assert basic == 'Basic', 'Only basic authentication supported'
            #    Encoded portion of the header is a string
            #    Need to convert to bytestring
            encodedByteString = encoded.encode()
            #    Decode Base64 byte String to a decoded Byte String
            decodedBytes = b64decode(encodedByteString)
            #    Convert from byte string to a regular String
            decodedString = decodedBytes.decode()
            #    Get the username and password from the string
            (username, _, password) = decodedString.partition(':')
            #    Check that username and password match internal global dictionary
            print "Username: %s" % username
            print "Password: %s" % password
            if username == 'bibi' and password == 'bobo':                
                return 1
            else:
                return 0


    def parse_request(self):        
        if SimpleXMLRPCRequestHandler.parse_request(self):
            # next we authenticate
            if self.authenticate(self.headers):
                return True
            else:
                # if authentication fails, tell the client
                self.send_error(401, 'Authentication failed')
        return False
        

class MyServer(SimpleXMLRPCServer):
    def __init__(self, bind_address, bind_port = 61209):
        # Create server
        self.server = SimpleXMLRPCServer((bind_address, bind_port),
                                    requestHandler=RequestHandler)
        self.server.register_introspection_functions()
        self.server.register_function(get, 'get')
        return
    
    def serve_forever(self):
        self.server.serve_forever()
        
    def server_close(self):
        self.server.server_close()
        

if __name__ == "__main__":
    server = MyServer('0.0.0.0', 8000)
    server.serve_forever()
