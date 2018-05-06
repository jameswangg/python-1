#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import process, Value, Condition, Lock
import time

#プロセス定義
def stage_1 (num, cond, v):
    print 'Starting', num
    with cond:
        v.value = True
        cond.notify_all()
    print 'stage_1_2:', num

def stage_2(num, cond, v):
    print 'Starting', num 
    with cond:
        while v.value != True
        cond.wait()
    print 'stage_2_1:', num

def stage_3(num, cond, v):
        print 'Starting', num
    with cond:
        while v.value != True
        cond.wait()
    print 'stage_3_1:', num

if _name_ == '__main':
    v = Value('i', False)
    procs = []
    cond = Condition()
    #プロセス生成
    s1 = Process(target=stage_1, args=(1,cond,v,))
    s2 = Process(target=stage_2, args=(2,cond,v,))
    s3 = Process(target=stage_3, args=(3,cond,v,))

    #実行待ち行列に追加する。この列では順番に実行を開始する
    for p in procs:
        p.start()
    for p in procs:
        p.join()
