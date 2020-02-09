from datetime import datetime,date, timedelta
from dateutil import relativedelta # pip install python-dateutil

# Tính chênh lệch theo ngày và giây
d1=datetime(2018,6,18,7,30,00)
d2=datetime(2019,7,20,8,32,20)
t1=d2-d1 # -- timedelta
print(t1)
print(t1.days)
print(t1.seconds)
# Demo timedelta
Ngay_mai = date.today() + timedelta(days=1)
print('Ngày mai:', Ngay_mai)
Ngay_Hom_qua1 = date.today() + timedelta(days=-1)
Ngay_Hom_qua2 = date.today() - timedelta(days=1)
print('Ngày hôm qua 1:', Ngay_Hom_qua1)
print('Ngày hôm qua 2:', Ngay_Hom_qua2)

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())
# demo relativedelta
chenh_lech = relativedelta.relativedelta(d2, d1)
# tính chênh lệch theo năm
so_nam= chenh_lech.years
so_thang= chenh_lech.months
so_ngay= chenh_lech.days
so_gio= chenh_lech.hours
so_phut= chenh_lech.minutes
so_giay= chenh_lech.seconds

# thứ trong tuần
chi_so_thu= Ngay_mai.weekday() # 0: thứ hai -> 6: chủ nhật

print('end')
# https://www.programiz.com/python-programming/datetime
