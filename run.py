#!/usr/bin/env python
# coding=utf-8

"""
@File：run.py
@Author：MicroKing
@Date：2020/2/13 13:23
@Desc:
"""
import os
from core import data_DXY, data_TX, common, merge_data

# 默认选项‘on’，自动运行；‘off’选项，关闭自动运行
@common.auto_runner('on')
def main():
    data_DXY.download()
    print('DXY json file download')
    data_TX.download()
    print('TX json file download')
    
    # 将每天的数据合并到一个文件
    # merge_data.merge_all()
    # print('data merged')


if __name__ == '__main__':
    main()
