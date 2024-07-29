#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from crypt import crypt
from string import printable
from itertools import product, count

def passwords(encoding):
    chars = [c.encode(encoding) for c in printable]
    for length in count(start=1):
        for pwd in product(chars, repeat=length):
            yield b''.join(pwd)

def crack(search_hash, encoding):
    for pwd in passwords(encoding):
        if crypt(pwd,'$6$' + salt) == search_hash:
            return pwd.decode(encoding)

if __name__ == "__main__":
    encoding = 'utf-8'#utf-8 for unicode support
    salt = 'e7Cuyti6'
    password_hash = '$6$e7Cuyti6$Iv336yy2LXR55DHnnyz5fd4A5wBJ2lhrUeaT9OZPZaQjjjWnF9TvFxiGBd6viAKCU.Q7IR5Mpgg4S9vtUA2501'
    cracked = crack(password_hash, encoding)
    print("Password cracked: " + cracked)
