#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from gzip import GzipFile

class MyStream(object):
    def write(self, data):
        #write to your stream...
        sys.stdout.write(data)#stdout for example

gz= GzipFile(fileobj=MyStream(), mode='w')
gz.write("something")
