#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, datetime

def main():
    while True:
        try:
            floatNow = time.time()
            print(floatNow)
            intFuture = (floatNow // 30) + 1
            print(intFuture)
            floatOffset = intFuture*30 - floatNow
            print(floatOffset)
            time.sleep(floatOffset)
            x = datetime.datetime.now()
            print(x.strftime("%a %w %b %X"))
        except KeyboardInterrupt:
            print(' received, shutting down server')

if __name__ == '__main__':
    main()
