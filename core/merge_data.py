#!/usr/bin/env python
# coding=utf-8

"""
@File：merge_data.py
@Author：MicroKing
@Date：2020/2/13 13:23
@Desc:
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_dir = f'{BASE_DIR}{os.sep}data{os.sep}json'


def load_data(f):
    with open(f, 'r', encoding='utf8') as fo:
        data = json.load(fo)
    return data 

def load_time(f):
    updatetime = f[9: 19]
    return updatetime

def merge(data_type):
    dir_path =f'{json_dir}{os.sep}json_{data_type.lower()}'
    file_ls = [fo for fo in os.listdir(dir_path) if data_type in fo]
    merge_data = [{'updatetime': load_time(f), 'data': load_data(f'{dir_path}{os.sep}{f}')} for f in file_ls]
    with open(f'{json_dir}{os.sep}COVID-19_(CN-DATA)by{data_type}.json', 'w', encoding='utf8') as fi:
        json.dump(merge_data, fi, indent='    ', ensure_ascii=False)

def merge_all():
    merge(data_type='TX')
    merge(data_type='DXY')

if __name__ =='__main__':
    
    pass
