# SpiderFramework
网络爬虫框架，可基于Raw包进行请求并回调拿到请求结果，支持自定义数据包
##  Install

``pip install spiderframework``

## Introduction
> 需要爬的功能类继承自BashGHCallback,如下（点赞和评论Instagram）:

重要的方法解释：

`api` : 要请求的Api接口

`reponse`: 请求成功之后的回调，包括Cookies 和 Content

`httpTypePost`: 是否操作Post请求

```python
# 评论
import os,sys
class GHComment(BaseGHCallback):
    def api(self):
        return 'https://www.instagram.com/web/comments/1465340700102125550/add/'
    def response(self,res):
        print res
if __name__ == '__main__':
        BaseGHCallback(GHComment).request()
```

## Usage

* pip install spiderframework 
* 继承BaseGHCallback
* 抓包或者通过其他自动化工具，将你的Raw信息保存到 `data`文件中。
* ``BaseGHCallback(class).httpRequest()``  发送Http请求，``reponse()``会回调请求结果
* ``BaseGHCallback(class).tcpRequest()``  发送tcp请求，response同上

## 自动化点赞和评论 [Instagram](https://github.com/xiyouMc/SpiderFramework/tree/master/Instagram)

如果觉得对你有帮助，麻烦Star。 么么哒 欢迎PR