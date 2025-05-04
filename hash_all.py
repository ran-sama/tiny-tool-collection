#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, hashlib, os
from os import listdir
from os.path import isfile, join
import time

mypath = "/media/kingdian/server_priv/yukari/"
os.chdir(mypath)
BUF_SIZE = 65536

def hashHelper(myinput):
    sha1 = hashlib.sha1()
    with open(myinput, 'rb') as f1:
        while True:
            data = f1.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    f1.close()
    f2.write(sha1.hexdigest() + " *" + myinput + "\r\n")
    print("Successful: " + sha1.hexdigest() + " *" + myinput)

print("Hashing files...")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
f2=open(str(int(time.time())) + ".sha1", "a+")
print("Printing to file...")
[hashHelper(i) for i in onlyfiles] 
f2.close()
print("All done...")
