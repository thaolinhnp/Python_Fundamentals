import calendar

laNamNhuan=calendar.isleap(2000)
thu = calendar.weekday(2019,3,15)
mr=calendar.monthrange(2019,3)

cs_thu_ngay_dau_thang=calendar.monthrange(2019,3)[0] #--> 4 (thứ 6)
soNgayTrongThang=calendar.monthrange(2019,3)[1] #--> 31

lichThang=calendar.monthcalendar(2019,3)
print(lichThang)
print('end')

"""
https://docs.python.org/3/library/calendar.html
"""