#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, hashlib, os

BUF_SIZE = 65536
os.chdir("/media/kingdian/server_priv/yukari/")
print("Hashing file...")

with open(sys.argv[1], 'rb') as f1:
    sha1 = hashlib.sha1()
    while True:
        data = f1.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)
f1.close()

print("Printing to file...")
f2=open(os.path.splitext(sys.argv[1])[0] + ".sha1", "w+")
f2.write(sha1.hexdigest() + " *" + sys.argv[1])
f2.close()

print("Successful: " + sha1.hexdigest() + " *" + sys.argv[1])
