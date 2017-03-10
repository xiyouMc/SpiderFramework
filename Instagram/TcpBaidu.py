import sys
import re
import os
sys.path.append("..")
from BaseGHCallback import BaseGHCallback
class GHRaw(BaseGHCallback):
    def api(self):
        return 'https://www.baidu.com/'
    def response(self,res):
        print res
if __name__ == '__main__':
    BaseGHCallback(GHRaw).tcpRequest()