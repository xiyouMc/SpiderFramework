#coding:utf-8
import sys
sys.path.append("../..")
import Request
# BaseGHCallback 基础类
class BaseGHCallback(object):
    call = None
    def __init__(self,Callback):
        self.call = Callback
    def api(self):
        pass
    def response(self,cookies,content):
        pass
    def request(self):
        Request.ghNetWork(self.call)
