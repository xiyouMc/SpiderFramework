import os,sys
sys.path.append("../../GHCrawFramwork")
from BaseGHCallback import BaseGHCallback
class GHComment(BaseGHCallback):
    def api(self):
        return 'https://www.instagram.com/web/comments/1465340700102125550/add/'
    def response(self,cookies,content):
        print content
class Query(BaseGHCallback):
    def api(self):
        return 'https://www.instagram.com/query/'
    def response(self,res):
        print res.text.encode('utf-8')
if __name__ == '__main__':
        # BaseGHCallback(GHComment).request()
        BaseGHCallback(Query).request()