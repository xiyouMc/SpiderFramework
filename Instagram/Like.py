import sys
import re
import os
# sys.path.append("..")
from BaseGHCallback import BaseGHCallback
class GHRaw(BaseGHCallback):
    def headersFile(self):
        return 'likeHeaders'
    def api(self):
        return 'https://www.instagram.com/web/likes/1449825299633270787/like/'
    def httpTypePost(self):
        return True
    def response(self,cookies,content):
        print content
if __name__ == '__main__':
    BaseGHCallback(GHRaw).request()