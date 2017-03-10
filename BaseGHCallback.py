#coding:utf-8
import sys
sys.path.append("../..")
import HttpRequest
import TCPRequest
'''
BaseGHCallback is a craw framework.
You can create a file with the name 'data', which stores raw data

>>> import BaseGHCallback
class Demo(BaseGHCallback):
    def api(self):
        return <api>
    def response(self,res):
        res.headers res.text.encode('utf-8')
BaseGHCallback(Demo).request()
'''
class BaseGHCallback(object):
    call = None
    def __init__(self,Callback):
        self.call = Callback
    '''
        return request`s api
    '''
    def api(self):
        pass
    '''
        Returns the result set of the request
    '''
    def response(self,res):
        pass
    '''
        BaseGHCallback(Demo).httpRequest()
    '''
    def httpRequest(self):
        HttpRequest.ghNetWork(self.call)
    '''
        BaseGHCallback(Demo).tcpRequest()
    '''
    def tcpRequest(self):
        TCPRequest.tcpRequest(self.call)