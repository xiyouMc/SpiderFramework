
import socket
import urlparse
import re
import os
# import socks
# import urllib2

socket.setdefaulttimeout = 0.50
os.environ['no_proxy'] = '127.0.0.1,localhost'
linkRegex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
CRLF = "\r\n\r\n"

def tcpRequest(RequestModel):
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"192.168.2.40",8880)
    # socket.socket =socks.socksocket
    # urllib2.urlopen(url).read()
    requestModel = RequestModel('')
    print(requestModel.api())
    url = urlparse.urlparse(requestModel.api())
    path = url.path
    if path == "":
        path = "/"
    HOST = url.netloc  # The remote host
    PORT = 80          # The same port as used by the server
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """
    ***********************************************************************************
    * Note that the connect() operation is subject to the timeout setting,
    * and in general it is recommended to call settimeout() before calling connect()
    * or pass a timeout parameter to create_connection().
    * The system network stack may return a connection timeout error of its own
    * regardless of any Python socket timeout setting.
    ***********************************************************************************
    """
    # s.settimeout(0.30)
    """
    **************************************************************************************
    * Avoid socket.error: [Errno 98] Address already in use exception
    * The SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state,
    * without waiting for its natural timeout to expire.
    **************************************************************************************
    """
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #s.setblocking(0)
    s.connect((HOST, PORT))
    f = open('data','r')
    lines = f.readlines()
    # print lines
    data = ''
    for line in lines:
        # print(str(line) + CRLF)
        data += str(line)
        # s.send()
    f.close()
    s.send(data)
    # s.send("GET / HTTP/1.0%s" % (CRLF))
    data = (s.recv(1024))
    # https://docs.python.org/2/howto/sockets.html#disconnecting
    s.shutdown(1)
    s.close()
    requestModel.response(data)
    # print 'Received', repr(data)

# class GHRaw(object):
#     def __init__(self,test):
#         pass
#     def api(self):
#         return 'https://www.baidu.com/'
#     def response(self,res):
#         print res
# if __name__ == '__main__':
#     tcpRequest(GHRaw)