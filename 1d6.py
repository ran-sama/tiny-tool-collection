#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

n_bytes = 5
dice_faces = 6
n_decimal = ((2**8)**n_bytes)/dice_faces
my_rolls = 1e5

def roll():
    my_dec = int.from_bytes(os.getrandom(n_bytes, os.GRND_NONBLOCK), byteorder='little', signed=False)
    if my_dec > n_decimal*5:
        return 6
    elif my_dec > n_decimal*4:
        return 5
    elif my_dec > n_decimal*3:
        return 4
    elif my_dec > n_decimal*2:
        return 3
    elif my_dec > n_decimal*1:
        return 2
    elif my_dec > 0:
        return 1
    elif my_dec == 0:
        print("rolled a 0 on a 6-faced dice")
        return roll()
    else:
        print("impossible")

def freq_analysis():
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0
    res6 = 0
    for x in range(int(my_rolls)):
        res = roll()
        if res == 1:
            res1 += 1
        if res == 2:
            res2 += 1
        if res == 3:
            res3 += 1
        if res == 4:
            res4 += 1
        if res == 5:
            res5 += 1
        if res == 6:
            res6 += 1
    return res1/my_rolls, res2/my_rolls, res3/my_rolls, res4/my_rolls, res5/my_rolls, res6/my_rolls

print("single roll test: ", roll())
print(freq_analysis())
