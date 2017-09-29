#取得現在的日期時間
from datetime import datetime #import library

print datetime.now() #print date of now
#看起來的output會長成：2013-11-25 23:45:14.317454

#也可以在now的變數下取得
current_year = datetime.now.year
current_month = datetime.now.month
current_day = datetime.now.day

print '%s-%s-%s' % (datetime.now.year, datetime.now.month, datetime.now.day)
#就可以改變時間的輸出方式

print '%s:%s:%s' % (datetime.now.hour, datetime.now.minute, datetime.now.second)
#或者輸出時間
