#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def roll():
    my_dec = int.from_bytes(os.getrandom(3, os.GRND_NONBLOCK), byteorder='little', signed=False)
    if my_dec > 5592405*2:
        return 3
    elif my_dec > 5592405:
        return 2
    elif my_dec > 0:
        return 1
    elif my_dec == 0:
        return roll()
    else:
        print("impossible")

def freq_analysis():
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    for x in range(int(1e5)):
        res = roll()
        if res == 0:
            res4 += 1
        if res == 1:
            res1 += 1
        if res == 2:
            res2 += 1
        if res == 3:
            res3 += 1
    return res1, res2, res3, res4

print(roll())
print(freq_analysis())
