#!/usr/bin/env python
# coding=utf-8

"""
@File：data_DXY.py
@Author：MicroKing
@Date：2020/2/13 13:23
@Desc:
1.爬取丁香园发布的新型冠状病毒肺炎的数据
"""
import os
import re
import requests
from bs4 import BeautifulSoup
import time
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 丁香园的肺炎疫情实时动态链接
dxy_url = 'https://3g.dxy.cn/newh5/view/' \
          'pneumonia?scene=2&clicktime=1579583352' \
          '&enterid=1579583352&from=timeline&isappinstalled=0'


def download(url=dxy_url):
    """
    爬取网页信息，将当日数据写入到json格式文件中
    :param url: -> string
    :return :None
    """
    # 发送请求，获得网页
    r = requests.get(url)
    assert r.status_code == 200
    
    # 解析网页，获得信息
    soup_object = BeautifulSoup(r.text, 'lxml')
    target_content = soup_object.select('body script#getAreaStat')
    target_content = target_content[0].get_text()
    target_content = re.findall('=.*', target_content)
    target_content = target_content[0].replace('= ', '')
    # 对信息重新解码
    data_str = target_content[:-11].encode('iso-8859-1').decode('utf8')
    # 将数据对象写入到json格式文件中，以日期为名称，保存到data\json目录下
    with open(f"{BASE_DIR}{os.sep}data{os.sep}json{os.sep}json_dxy{os.sep}COVID-19_{time.strftime('%Y-%m-%d')}(CN-DATA)"
              f"by_DXY.json", 'w', encoding='utf8') as f:
        json.dump(json.loads(data_str), f, ensure_ascii=False, indent='    ')

   
def download_country_data(url=dxy_url):
    r = requests.get(url)
    assert r.status_code == 200
    
    # 解析网页，获得信息
    soup_object = BeautifulSoup(r.text, 'lxml')
    target_content = soup_object.select('body script#getListByCountryTypeService2true')
    target_content = target_content[0].get_text()
    target_content = re.findall('=.*', target_content)
    target_content = target_content[0].replace('= ', '')
    # 对信息重新解码
    data_str = target_content[:-11].encode('iso-8859-1').decode('utf8')
    # 将数据对象写入到json格式文件中，已日期为名称，保存到Data\JSON目录下
    with open(f"{BASE_DIR}{os.sep}data{os.sep}json{os.sep}COVID-19_{time.strftime('%Y-%m-%d')}"
              f"by_DXY_country.json", 'w', encoding='utf8') as f:
        json.dump(json.loads(data_str), f, ensure_ascii=False, indent='    ')
if __name__ == '__main__':
    pass