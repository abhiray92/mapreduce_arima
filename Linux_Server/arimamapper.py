#!/usr/bin/python3

import sys
import os
from datetime import datetime
import math

header_skipped = False

for record in sys.stdin :
    date,time, gae = record.rstrip('\n').split(',')

    if header_skipped : # skip header
        date_str = datetime.strptime(date,'%d/%m/%Y')
        time_str = datetime.time(datetime.strptime(time,'%H:%M:%S'))
        dt_str = datetime.combine(date_str, time_str)
        date_time_string = datetime.strftime(dt_str,'%Y%m%d%H%M')
        print('{}\t{}'.format(date_time_string,round(float(gae),2)))
    header_skipped = True
