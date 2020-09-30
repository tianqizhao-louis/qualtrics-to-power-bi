'''
    This file is used to extract responses every 20 seconds,
    corporating with Qualtrics_API.py
'''

import time
import Qualtrics_API

# setting timer
def sleeptime(hour, min, sec):
    return hour*360 + min * 60 + sec

# get it run every 20 seconds
second = sleeptime(0,0,20)

# run
while 1 == 1:
    time.sleep(second)
    Qualtrics_API.extract()
