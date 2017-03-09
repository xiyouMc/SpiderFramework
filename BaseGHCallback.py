#coding:utf-8
import sys
sys.path.append("../..")
import Request
# BaseGHCallback 基础类
class BaseGHCallback(object):
    call = None
    def __init__(self,Callback):
        self.call = Callback
    def headersFile(self):
        pass
    def cookies(self):
        pass
    def data(self):
        pass
    def api(self):
        pass
    def httpTypePost(self):
        return True
    def response(self,cookies,content):
        pass
    def request(self):
        Request.ghNetWork(self.call)
