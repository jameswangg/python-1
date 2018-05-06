    #! /usr/bin/env python
    # -*- coding: utf-8 -*-
from multiprocessing import Process, Value, Lock
import time

#プロセスの定義
def worker (num, val):
    for i in range(50): #50回ループ
        val.value += 1 #valは共有変数。これを +1 する
        #print("Pid:", num, ":", val.value)

if _name_ == '_main_':
    v = Value('i', 0) #共有変数を作る
    lock = Lock() 
    procs = [] #プロセスを入れておく配列

    for i in range(10): #10個作る
        p = Process(target=worker, args=(i,v,))　#Processを生成。引数は番号と共有変数
        procs.append(p) #配列に追加

    for p in procs: #作ったプロセスの実行を開始する
        p.start() 

    for p in procs: #全部の終了を待つ
        p.join()

    for p in procs:
        p.lock.aquire()

    for p in procs:
        p.lock.release()

print v.value　#共有変数を用意する

#ライン１8にエラーが発生
