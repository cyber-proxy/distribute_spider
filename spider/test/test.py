#coding=utf-8
import requests as req;
import sys
from bs4 import BeautifulStoneSoup as bfs
import lxml
import pyquery
import json
import scrapy as spy

url = "https://v.taobao.com/v/content/live?catetype=704&from=taonvlang"

webReq = req.get(url)
print webReq.content

bsObj = bfs(webReq.content)
aList = bsObj.find_all("img")
for a in aList:
    print a.get('src')


def parse_index():
    session = req.Session()
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://mm.taobao.com',
        'referer': 'https://mm.taobao.com/search_tstar_model.htm',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'q': '',
        'viewFlag': 'A',
        'sortType': 'default',
        'searchStyle': '',
        'searchRegion': 'city:',
        'searchFansNum': '',
        'currentPage': '1',
        'pageSize': '100',
    }

    resp = session.post(url=url, data=data, headers=headers)
    print req
