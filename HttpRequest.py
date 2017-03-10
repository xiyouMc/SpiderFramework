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
def ghNetWork(RequestModel):
    call = RequestModel('')
    headers,data,httpPost = headerAndBody()
    _result = requests.post(call.api(), headers=headers,data=data) if httpPost else requests.get(call.api(), headers=headers,data=data)
    call.response(_result)

def headerAndBody():
    if not os.path.exists('data'):
        logging.error('not have data file')
        return '','',''
    f = open('data','r')
    lines = f.readlines()
    f.close()
    httpPost = True
    header = {}
    params = ''
    cookies = '' 
    body = ''
    for index in range(len(lines)): 
        ii = lines[index].split(':',1)
        if len(ii) == 2 and not ii[0]=='':
                if ii[0] == 'cookie':
                    cookies += ii[1].strip() + ';'
                    continue
                key = ii[0]
                value = ii[1].strip()
                header[key] = value
        header['cookie'] = cookies
        if index == 0:
            if 'POST' in lines[index]:
                print('Post Request')
                # Get body 
                httpPost = True
            else:
                print('Get Request')
                httpPost = False
                params = lines[index].split(' ')[1]
        if httpPost and index == len(lines) -1:
            body = lines[index]
            
    return header,params if not params == '' else body,httpPost
if __name__ == '__main__':
    headers,params,httpPost = headerAndBody()
    print headers,params,httpPost
    # for (k,v) in headers.items():
    #      print(str(i) + " " + params)
   