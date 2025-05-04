#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, requests

my_list = []
url = "https://raw.githubusercontent.com/mozilla/cookie-banner-rules-list/main/cookie-banner-rules-list.json"

def main():
    r = requests.get(url)
    j = r.json()
    for key1 in j['data']:
        for key in key1['domains']:
            my_list.append(key)
    my_list.sort()
    for item in my_list:
        print(item)
    pass

if __name__ == '__main__':
    main()
