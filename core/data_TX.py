#!/usr/bin/env python
# coding=utf-8

"""
@File：data_TX.py
@Author：MicroKing
@Date：2020/2/14 14:39
@Desc:
1.爬取腾讯发布的新型冠状病毒肺炎的数据
"""
import os
import requests
import time
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tx_url = f'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_1580701479520&_={int(time.time() * 1000)}'


def download(url=tx_url):
    r = requests.get(url)
    assert r.status_code == 200
    data_str = r.json()['data']
    with open(f"{BASE_DIR}{os.sep}data{os.sep}json{os.sep}json_tx{os.sep}COVID-19_{time.strftime('%Y-%m-%d')}(CN-DATA)by_TX.json", 'w', encoding='utf8') as f:
        json.dump(json.loads(data_str), f, ensure_ascii=False, indent='    ')


if __name__ == '__main__':
    pass