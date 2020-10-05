#!/usr/bin/python3
#wma_reducer.py

import os
import sys
from datetime import timedelta, datetime
from math import sqrt
from slidingwindow import SlidingARIMA

last_observation = ''

window = SlidingARIMA(10000,None)

absolute_error = float(0)
squared_error = float(0)
absolute_percentage_error = float(0)
count = int(0)

print('date/time\tactual\tforecast')
for record in sys.stdin :
    try: 
        key,value = record.rstrip(os.linesep).split('\t')
        date_time_string,rowtype = key.split('|')
        date_time = datetime.strptime(date_time_string,'%Y%m%d%H%M')
        date_time_out = datetime.strftime(date_time,'%d/%m/%Y %H:%M')
        if rowtype == 'F' :
           actual, forecast = value.split('|')
           print('{}\t{}\t{}'.format(date_time_out,actual,forecast))
           absolute_error = absolute_error + abs(float(actual)-float(forecast))
           squared_error = squared_error + (float(actual)-float(forecast))**2
           absolute_percentage_error = float(absolute_percentage_error + (float(actual) - float(forecast))/sys.float_info.min if actual == 0 else actual)
           count = count + 1
        else :
            if last_observation == date_time_string :
                window.append(value)
                if window.is_full() :
                    print('{}\t{}\t{}'.format(date_time_out,value,window.predict()))
                    absolute_error = absolute_error + abs(value-window.predict())
                    squared_error = squared_error + (value-window.predict())**2
                    absolute_percentage_error = float(absolute_percentage_error + (float(value) - float(window.predict()))/sys.float_info.min if value == 0 else value)
                    count = count + 1
            else :
                window.clear()
                window.append(value)         
            last_observation = date_time_string
    except Exception as e:
        print(e)
print('Mean Absolute Error\t{:.3f}'.format(absolute_error/count))
print('Root Mean Squared Error\t{:.3f}'.format(sqrt(squared_error/count)))
print('Mean Absolute Percentage Error\t{:.3f}'.format(absolute_percentage_error/count))
