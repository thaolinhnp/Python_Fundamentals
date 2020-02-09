from datetime import datetime,date

ngayHienHanh1=datetime.today()
ngayHienHanh2=date.today()

thoiDienHienHanh=datetime.now()

tpNgay=ngayHienHanh2.day
tpThang=ngayHienHanh2.month
tpNam=ngayHienHanh2.year

ngaySinh=datetime(1991,6,25)

# Chuyển biểu thức ngày thành chuỗi theo định dạng
s1=ngayHienHanh1.strftime("%d/%m/%y")
s2=ngayHienHanh1.strftime("%d/%m/%Y")
s3=ngayHienHanh1.strftime("%A %d %B %y")

s4=ngayHienHanh1.strftime("%H:%M:%S")

# Chuyển chuỗi thành biểu thức ngày (datetime)
str_ngaySinh= "25-06-1991"
ngaySinh=datetime.strptime(str_ngaySinh,"%d-%m-%Y")

print(dir(datetime))
print('end')