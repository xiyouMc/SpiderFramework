#coding:utf-8
from datetime import datetime
import logging
import requests
import json
import time
import os
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='cataline.log',
    filemode='w')
#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################
def ghNetWork(callback):
    call = callback('')
    _result = requests.post(call.api(), headers=headers(call.headersFile()),data=call.data()) if call.httpTypePost() else requests.get(call.api(), headers=call.headers(), params=call.data())
    call.response( _result.headers.get('set-Cookie'), _result.text.encode('utf-8'))
def headers(headersFile):
    f = open(headersFile,'r')
    headers = f.readlines()
    f.close()
    header = {}
    cookies = ''
    for i in headers:
        ii = i.split(':',1)
        if len(ii) == 2 and not ii[0]=='':
             if ii[0] == 'cookie':
                 cookies += ii[1].strip() + ';'
                 continue
             key = ii[0]
             value = ii[1].strip()
             header[key] = value
    header['cookie'] = cookies
    return header