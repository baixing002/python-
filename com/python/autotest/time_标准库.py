"""
time 常用时间模块
"""

import time

#国外的时间格式
# print(time.asctime())
# print(time.time())
print(time.localtime())
# print(time.strftime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.strftime("%Y:%m:%d %H:%M:%S",time.localtime()))
# print(time.strftime("%Y年%m月%d日 %H:%M:%S",time.localtime()))
# UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: Illegal byte sequenc

# 获取两天前的时间
#当前时间
now_timestamp = time.time()
#两天前秒数
two_day_before = now_timestamp - 60*60*24*2
#秒换算成时间点
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y:%m:%d %H:%M:%S", time_tuple))

#三天后的时间