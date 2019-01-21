#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib
import json
import vim
from urllib import request as urllib

appId="23c5f65c598f21c5"
appPwd="ywspAhm4qA58rDT0P8yKJCsSpXDHBE0z"
url="http://openapi.youdao.com/api?q=%s&appKey=%s&salt=%s&sign=%s"

def searchExplainByPython():
    words=vim.eval('a:words').strip()
    salt="ts"
    toBeSignStr=appId+words+salt+appPwd
    sign=getMd5(toBeSignStr)
    
    queryUrl=url % (urllib.quote(words),appId,salt,sign)
    dataBack = urllib.urlopen(queryUrl).read().decode('utf-8')
    try:
        dataJson = json.loads(dataBack)
        showData(dataJson,words)
    except ValueError:
        print(cData['errorCode']['noQuery'])
    print(dataJson)

def getMd5(toBeStr):
    md5=hashlib.md5()
    md5.update(bytes(toBeStr,encoding = "utf8"))
    return md5.hexdigest()
def showData(rs,words):
    cwin=vim.eval('search#GetExplainWindowID()') 
    vim.command(cwin+' wincmd w')
    cbuf=vim.current.buffer
    vim.command('setl modifiable')
    vim.command('%d _')

    if rs["errorCode"] != '0':
        cbuf.append(words+" ===>Translate Failure(翻译失败)")
    else:
        translations=""
        for item in rs["translation"]:
            translations+=item+" "
        cbuf.append(words+" ===>"+translations)

    vim.command('0d _')
    vim.command('setl nomodifiable')

__all__ = ['searchExplainByPython']
