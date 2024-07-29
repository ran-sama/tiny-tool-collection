#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, time, errno, sys

def main():
    print("Starting entropy streamer!")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8888))
    s.listen(100)
    while True:
        (insock, address) = s.accept()
        sys.stdout.write('%s - %s:%d' % (time.ctime(), address[0], address[1]))
        try:
            sent = 0
            justblocked = 0
            hwrngFile = open('/dev/hwrng', 'r')
            while (justblocked != 1):
                sent = insock.send(hwrngFile.read(64000))
                if sent == 0:
                    justblocked = 1
                    sys.stdout.write(" [\033[91mFAILED\033[0m]")
            insock.shutdown(socket.SHUT_RDWR)#socket.SHUT_RDWR or 2
            insock.close()
        except socket.error, e:
            pass
            sys.stdout.write(' Error: %s' % (e))
            print(" [\033[93mDEPEND\033[0m]")
        else:
            print (" [  \033[92mOK\033[0m  ]")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Bye!'
        exit(0)
    except BaseException, e:
        sys.stdout.write(' Base Exception: %s' % (e))
        exit(1)
