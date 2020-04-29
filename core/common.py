#!/usr/bin/env python
# coding=utf-8

"""
@File：common.py
@Author：MicroKing
@Date：2020/2/13 13:23
@Desc:
"""
import time

def second_to_hms(t):
    """
    将总秒数t换算为 H:M:S 的形式
    :param t: -> float
    :return info: string
    """
    h, m_s = divmod(int(t), 3600)
    m, s = divmod(m_s, 60)
    info = f'{h:0>2.0f}:{m:0>2.0f}:{s:0>2.0f}'
    return info

# 控制程序每天在设定的时间自动运行一次
def auto_runner(status='on'):
    def wrapper(func):
        def inner(*args, **kwargs):
            if status == 'off':
                print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 程序<{func.__name__}>开始执行。。。')
                return func(*args, **kwargs)
            while True:
                # second_count 用于设置程序执行的时间，例如：
                # 设置为300时，对应时间为23:55:00，即24点整扣除300s后对应的时间
                second_count = 300
                seconds = ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time()) - second_count
                print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 程序<{func.__name__}>将在 {second_to_hms(t=seconds)} 后执行')

                while ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time()) - second_count > 0:
                    tmp_t = ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time()) - second_count
                    time.sleep(tmp_t)
                    #info = second_to_hms(t=tmp_t)
                    #print(f'等待时长: {info}', end='\r')
                else:
                    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 程序<{func.__name__}>开始执行。。。')
                    func(*args, **kwargs)
                    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 程序<{func.__name__}>当日执行完成。。。')

                sleep_seconds = ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time())
                print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 程序<{func.__name__}>将在 {second_to_hms(t=sleep_seconds)} 后进入新的执行过程。。。')    
                time.sleep(sleep_seconds)
                #while ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time()) - second_count < 0:    
                #    tmp_t = ((time.time() + 8 * 3600) // 86400 + 1) * 86400 - 8 * 3600 - int(time.time()) - second_count
                    #info = second_to_hms(t=tmp_t)
                    #print(f'等待时长: {info}', end='\r')
        return inner
    return wrapper
