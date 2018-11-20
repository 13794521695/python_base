import  time
print(time.time())          #时间戳是从1970 1月1日 零点
print(time.ctime())  #打印 Sat Sep 22 10:32:33 2018
print(time.localtime()) #打印时间元祖，time.struct_time(tm_year=2018, tm_mon=9, tm_mday=22, tm_hour=10, tm_min=34, tm_sec=16, tm_wday=5, tm_yday=265, tm_isdst=0)
print(time.localtime(1)) #和上面的格式一样，不过是1970 1-1 零点
print(time.gmtime())  # 和localtime打印的一致
tmp_time = time.localtime()
print(tmp_time.tm_year)   #会打印2018

print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime()))  #打印2018-09-22  10:42:39
print(time.strptime('2011-11-11 11:11:12','%Y-%m-%d   %H:%M:%S'))


#datetime
from  datetime import  datetime,time,date,timedelta
print(datetime.now())   #打印2018-09-22 10:50:03.044910
tmp_date = datetime(2017,11,11,11,11,11)
print(tmp_date)
print(date.today())
print()
