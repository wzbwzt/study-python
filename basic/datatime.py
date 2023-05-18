from dateutil import parser
import numpy as np
import datetime
from dateutil import parser

'''
datetime 是 Python 中处理日期的标准模块，它提供了 4 种对日期和时间进行处理的类：datetime、date、time 和
timedelta
'''
# datetime类
'''
1. datetime.now(tz=None) 获取当前的日期时间，输出顺序为：年、月、日、时、分、秒、微秒。
2. datetime.timestamp() 获取以 1970年1月1日为起点记录的秒数。
3. datetime.fromtimestamp(tz=None) 使用 unixtimestamp 创建一个 datetime。
'''

dt = datetime.datetime(year=2020, month=6, day=25,
                       hour=11, minute=23, second=59)
print(dt)  # 2020-06-25 11:23:59
print(dt.timestamp())  # 1593055439.0
dt = datetime.datetime.fromtimestamp(1593055439.0)
print(dt)  # 2020-06-25 11:23:59
print(type(dt))  # <class 'datetime.datetime'>
dt = datetime.datetime.now()
print(dt)  # 2020-06-25 11:11:03.877853
print(type(dt))  # <class 'datetime.datetime'>


'''
datetime.strftime(fmt) 格式化 datetime 对象。

%a 本地简化星期名称（如星期一，返回 Mon）
%A 本地完整星期名称（如星期一，返回 Monday）
%b 本地简化的月份名称（如一月，返回 Jan）
%B 本地完整的月份名称（如一月，返回 January）
%c 本地相应的日期表示和时间表示
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%j 年内的一天（001-366）
%m 月份（01-12）
%M 分钟数（00-59）
%p 本地A.M.或P.M.的等价符
%S 秒（00-59）
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（0000-9999）
%Z 当前时区的名称（如果是本地时间，返回空字符串）
%% %号本身
'''
# 自定义输出格式
dt = datetime.datetime(year=2020, month=6, day=25,
                       hour=11, minute=51, second=49)
s = dt.strftime("'%Y/%m/%d %H:%M:%S")
print(s)  # '2020/06/25 11:51:49
s = dt.strftime('%d %B, %Y, %A')
print(s)  # 25 June, 2020, Thursday

'''
1. datetime.date() Return the date part.
2. datetime.time() Return the time part, with tzinfo None.
3. datetime.year 年
4. datetime.month 月
5. datetime.day 日
6. datetime.hour 小时
7. datetime.minute 分钟
8. datetime.second 秒
9. datetime.isoweekday 星期几
'''
dt = datetime.datetime(year=2020, month=6, day=25,
                       hour=11, minute=51, second=49)
print(dt.date())  # 2020-06-25
print(type(dt.date()))  # <class 'datetime.date'>
print(dt.time())  # 11:51:49
print(type(dt.time()))  # <class 'datetime.time'>
print(dt.year)  # 2020
print(dt.month)  # 6
print(dt.day)  # 25
print(dt.hour)  # 11
print(dt.minute)  # 51
print(dt.second)  # 49
print(dt.isoweekday())  # 4

'''parser.parse(timestr, parserinfo=None, **kwargs)


'''
s1 = "2010 Jan 1"
s2 = '31-1-2000'
s3 = 'October10, 1996, 10:40pm'
dt1 = parser.parse(s1)
dt2 = parser.parse(s2)
dt3 = parser.parse(s3)
print(dt1)  # 2010-01-01 00:00:00
print(dt2)  # 2000-01-31 00:00:00
print(dt3)  # 1996-10-10 22:40:00


# 计算以下列表中连续的天数
dateString = ['Oct, 2, 1869', 'Oct, 10, 1869',
              'Oct, 15, 1869', 'Oct, 20, 1869', 'Oct, 23, 1869']
dates = [parser.parse(i) for i in dateString]
td = np.diff(dates)
print(td)
# [datetime.timedelta(days=8) datetime.timedelta(days=5)
# datetime.timedelta(days=5) datetime.timedelta(days=3)]
d = [i.days for i in td]
print(d)  # [8, 5, 5, 3]

# date类
'''
date.today() 获取当前日期信息

'''

d = datetime.date(2020, 6, 25)
print(d)  # 2020-06-25
print(type(d))  # <class 'datetime.date'>
d = datetime.date.today()
print(d)  # 2020-06-25
print(type(d))  # <class 'datetime.date'>

# 计算d1和d2之间有多少星期六
d1 = datetime.date(1869, 1, 2)
d2 = datetime.date(1869, 10, 2)
dt = (d2 - d1).days
print(dt)
print(d1.isoweekday())  # 6
print(dt // 7 + 1)  # 40

# time类
t = datetime.time(12, 9, 23, 12980)
print(t)  # 12:09:23.012980
print(type(t))  # <class 'datetime.time'>


# e,g,将给定时间转换为当天的开始时间
date = datetime.date(2019, 10, 2)
print(date)
dt = datetime.datetime(date.year, date.month, date.day)
print(dt)  # 2019-10-02 00:00:00
dt = datetime.datetime.combine(date, datetime.time.min)
print(dt)  # 2019-10-02 00:00:00

# timedelta类
'''
表示具体时间实例中的一段时间。你可以把它们简单想象成两个日期或时间之间的间隔。
它常常被用来从 datetime 对象中添加或移除一段特定的时间。

如果将两个 datetime 对象相减，就会得到表示该时间间隔的 timedelta 对象。
同样地，将两个时间间隔相减，可以得到另一个 timedelta 对象
'''
# e.g.
td = datetime.timedelta(days=30)
print(td)  # 30 days, 0:00:00
print(type(td))  # <class 'datetime.timedelta'>
print(datetime.date.today())  # 2020-07-01
print(datetime.date.today() + td)  # 2020-07-31
dt1 = datetime.datetime(2020, 1, 31, 10, 10, 0)
dt2 = datetime.datetime(2019, 1, 31, 10, 10, 0)
td = dt1 - dt2
print(td)  # 365 days, 0:00:00
print(type(td))  # <class 'datetime.timedelta'>
td1 = datetime.timedelta(days=30)  # 30 days
td2 = datetime.timedelta(weeks=1)  # 1 week
td = td1 - td2
print(td)  # 23 days, 0:00:00
print(type(td))  # <class 'datetime.timedelta'>
