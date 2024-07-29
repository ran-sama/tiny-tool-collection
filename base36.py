#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

n_bytes = 32
my_rolls = 10

__version__ = '1.0.0'
__all__ = ['dumps', 'loads']

if sys.version_info.major == 2:
    integer_types = (int, long)
else:
    integer_types = (int,)

alphabet2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
my_int= int(32069055419758846538414151281338716380419187659620367979971160421596771143528976055857477413617556226582761999477251)

def dumps(number):
    if not isinstance(number, integer_types):
        raise TypeError('number must be an integer')

    if number < 0:
        return '-' + dumps(-number)

    value = ''

    while number != 0:
        number, index = divmod(number, len(alphabet))
        value = alphabet[index] + value

    return value or '0'

def loads(value):
    return int(value, 36)

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

def freq_analysis():
    for x in range(int(my_rolls)):
        my_dec = int.from_bytes(os.getrandom(n_bytes, os.GRND_NONBLOCK), byteorder='little', signed=False)
        print(encrypt(dumps(my_dec),5))

freq_analysis()
