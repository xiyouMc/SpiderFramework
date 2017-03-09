import os,sys
sys.path.append("..")
from BaseGHCallback import BaseGHCallback
class GHComment(BaseGHCallback):
    def headersFile(self):
        return 'CommentHeaders'
    def api(self):
        return 'https://www.instagram.com/web/comments/1465340700102125550/add/'
    def data(self):
        return {'comment_text':'Wow'}
    def response(self,cookies,content):
        print content
if __name__ == '__main__':
        BaseGHCallback(GHComment).request()