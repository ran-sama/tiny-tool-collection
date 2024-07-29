#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, dns.resolver
from gpiozero import LED
from datetime import datetime

led0 = LED(19)#gelb
led1 = LED(13)#blau
led2 = LED(26)#lila

def lights_off():
    led1.off()
    led2.off()
    led0.off()

def dns_query_specific_nameserver1(query="domain1.example.com", nameserver="10.0.0.7", qtype="A"):
    try:
        lights_off()
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [nameserver]
        answer = resolver.resolve(query, qtype)
        if len(answer) == 0:
            led0.on()
            time.sleep(2)
        else:
            led1.on()
            return str(answer[0])
    except dns.exception.Timeout:
        print("Major exception at: " + datetime.now().isoformat())
        led0.on()
        time.sleep(2)

def dns_query_specific_nameserver2(query="domain2.example.com", nameserver="10.0.0.24", qtype="A"):
    try:
        lights_off()
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [nameserver]
        answer = resolver.resolve(query, qtype)
        if len(answer) == 0:
            led0.on()
            time.sleep(2)
        else:
            led2.on()
            return str(answer[0])
    except dns.exception.Timeout:
        print("Major exception at: " + datetime.now().isoformat())
        led0.on()
        time.sleep(2)

def main():
    while True:
        try:
            dns_query_specific_nameserver1(qtype="A")
            time.sleep(0.1)
            dns_query_specific_nameserver2(qtype="A")
            time.sleep(0.1)
            lights_off()
            floatNow = time.time()
            intFuture = (floatNow // 30) + 1
            floatOffset = intFuture*30 - floatNow
            time.sleep(floatOffset)
        except KeyboardInterrupt:
            print("Terminated manually.")
            quit()

if __name__ == '__main__':
    main()
