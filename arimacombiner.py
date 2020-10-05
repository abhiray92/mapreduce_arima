#!/usr/bin/python3

from datetime import datetime, timedelta
from decimal import *
from slidingwindow import SlidingARIMA
import sys
import os

window = SlidingARIMA(60,None)

for record in sys.stdin :
    try: 
        date_time_string,gae = record.rstrip(os.linesep).split('\t')
        gae = Decimal(gae)
        window.append(gae)
        if window.is_full():
            # pass the forecast for the complete window to the reducer
            print('{}|F\t{}|{}'.format(date_time_string,gae,round(window.predict(),2)))
        else :
            # pass incomplete window at the start of the series to the reducer
            for index in range(0,len(window)) :
                print('{}|B\t{}'.format(date_time_string,window[index]))
    except Exception as e:
        print(e)

date_time = datetime.strptime(date_time_string,'%Y%m%d%H%M')    

# pass incomplete window at the end of the series to the reducer
for observation in reversed(range(1,len(window))) :
    observations = list(window)[0:len(window)]
    date_time = date_time+timedelta(hours = 1)
    date_time_out = datetime.strftime(date_time,'%Y%m%d%H%M')
    for index in reversed(range(1,len(observations))) :
        print('{}|E\t{}'.format(date_time_out,observations[index]))
    window.pop()

