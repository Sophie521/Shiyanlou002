#! /usr/bin/env python3

from multiprocessing import Process, Pipe, Queue
import sys
import csv
from decimal import Decimal as D

arg = {}
i = sys.argv
arg[i[1]] = i[2]
arg[i[3]] = i[4]
arg[i[5]] = i[6]


def f(s):
    if s <= 0:
        return 0.0
    if s <= 1500:
        return s * 0.03
    if 1500 < s <= 4500:
        return s * 0.1 - 105
    if 4500 < s <= 9000:
        return s * 0.2 - 555
    if 9000 < s <= 35000:
        return s * 0.25 - 1005
    if 35000 < s <= 55000:
        return s * 0.3 - 2755
    if 55000 < s <= 80000:
        return s * 0.35 - 5505
    else:
        return s * 0.45 - 13505


def f_bili(s):
    with open(s) as f:
        global d
        d = {}
        for i in f:
            d[i.split(' ')[0]] = i.split(' ')[2]
        bl = 0
        for j in d.values():
            if float(j) > 1:
                continue
            bl += float(j)
        return bl


def f_gz(s):
    with open(s) as f:
        gz = {}
        for i in csv.reader(f):
            gz[i[0]] = int(i[1])
    q1.put(gz)


def shebao_geshui():
    bl = f_bili(arg['-c'])
    gz = q1.get()
    ans_d = []
    for i in gz:
        ans = []
        a = gz[i]
        ans.append(i)
        ans.append(a)
        if a < float(d['JiShuL']):
            shebao = bl * float(d['JiShuL'])
        if a > float(d['JiShuH']):
            shebao = float(d['JiShuH']) * bl
        else:
            shebao = a * bl
        ans.append(D(shebao).quantize(D('0.00')))
        s = gz[i] - shebao - 3500
        ans.append(D(f(s)).quantize(D('0.00')))
        ans.append(D(gz[i] - shebao - f(s)).quantize(D('0.00')))
        ans_d.append(ans)
        q2.put(ans_d)


def xieru_gzd():
    with open(arg['-o'], 'w') as ff:
        w = csv.writer(ff)
        w.writerows(sorted(q2.get()))


if __name__ == '__main__':

    q1 = Queue()
    q2 = Queue()
    p1 = Process(target=f_gz, args=(arg['-d'],))
    p2 = Process(target=shebao_geshui)
    p3 = Process(target=xieru_gzd)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join
