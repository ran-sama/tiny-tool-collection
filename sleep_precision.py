from datetime import datetime
import time

def check_sleep(amount):
    start = datetime.now()
    time.sleep(amount)
    end = datetime.now()
    delta = end-start
    return delta.seconds + delta.microseconds/1000000.

error = sum(abs(check_sleep(0.050)-0.050) for i in xrange(100))*10
print("Average error is %0.2fms" % error)
