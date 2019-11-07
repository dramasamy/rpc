import xmlrpclib
import socket

def _get_rpc():
    a = xmlrpclib.ServerProxy('http://dd:LNXFhcZnYshy5mKyOFfy@127.0.0.1:9001')

    try:
        a._()   # Call a fictive method.
    except xmlrpclib.Fault:
        # connected to the server and the method doesn't exist which is expected.
        pass
    except socket.error:
        # Not connected ; socket error mean that the service is unreachable.
        return False, None

    # Just in case the method is registered in the XmlRPC server
    return True, a

connected, server_proxy = _get_rpc():
if not connected
    print "Failed to connect"
    import sys
    sys.exit(1)
