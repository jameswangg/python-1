
#-*- coding: utf-8 -*-
from multiprocessing import Process, cpu_count 
import time

# ただカウントダウンするプロセス 
def worker(n):     
    while n > 0:
        n -= 1 

# ここからメイン関数 
if __name__ == '__main__':     
    procs = []  # プロセス配列     
    num = 1     # 利⽤プロセス数 

    #cpuのコア数を表示
    print("# of physical cores:", cpu_count())

    n = []
    m = int(2e8) # 200M = 2億
    for i in range(num):
        n.append(int(m/num))

    #利用プロセス数分プロセスを起動する
    for i in range(num):
        p = Process(target=worker, args=(n[i],)) 
        procs.append(p)

    #開始時間
    start_time = time.time()

    #プロセススタート
    for j in procs:
        j.start()

    #プロセス終了待ち
    for j in procs:
        j.join()

    #終了時間
    finish_time = time.time()

    #かかった時間を表示
    print(finish_time - start_time)

    #(1) このプログラムを実⾏してみよ。実⾏時間はいくつになるか？
    #
    #基本的に１－9秒かかります、パイソンだと１０個あるはずですので
    #それに関係しているのではと思います。
    #
    #(2) 別ウィンドウでtop コマンドを実⾏して、numの値を1〜10まで変えて実⾏してみよう。 値はどう変化するか？ 
    #
    #タスクマネジャーを調べる
    #１０個(0-9)の整数が出てきて奇数はいつも偶数より多いようですが値の数自体が実行する度に代わってくることもあります。
    #
    #(3) なぜそうなるのかで考えられる理由を簡単にかけ
    #
    #１－９の値に限られているからだと思います。０はインデックスによるものです。
    #





