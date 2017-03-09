# SpiderFramework
网络爬虫框架，可基于Raw包进行请求和返回，并支持自定义数据包

# BaseGHCallback.py
> 需要爬的功能类继承自BashGHCallback,如下（点赞和评论Instagram）:

* 重要的方法解释：

`headersFile` : raw包的数据，可通过其他自动化脚本或者抓包填充
`api` : 要请求的Api接口
`data`: Post请求使用的数据
`reponse`: 请求成功之后的回调，包括Cookies 和 Content
`httpTypePost`: 是否操作Post请求

```python
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
```

## Useage

> 你需要做的就是去抓包或者通过其他自动化工具，将你的Headers信息填充到对应文件。  并通过 ``headersFile``返回该文件目录。

``BaseGHCallback(class).request()``  发送请求，``reponse()``会回调请求结果