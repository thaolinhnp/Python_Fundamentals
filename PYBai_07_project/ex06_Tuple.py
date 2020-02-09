# Khởi tạo tuple
daySo = (200, 10, 30, 100)
daySo2 = 200, 10, 30, 100
danhSachTen = ("Tâm", "Thanh", "Bình")
danhSach = (9, 'abc', True)
# Khởi tạo tuple rổng
tupleR=()

# Khởi tạo tuple có 1 phần tử với giá trị là 30
tuple_1=(30,)
# In danh sách
print(danhSachTen)
print(daySo)
print(danhSach)
 
# Tổng số phần tử
tongspt = len(daySo)
print('Tổng số phần tử:', tongspt)
 
# Truy xuất giá trị phần tử
print(daySo[0])
print(danhSachTen[1])
print(danhSachTen[-1])
 
# Ghép dữ liệu các tuple --> tạo ra tuple mới
ds1 = (1, 3, 5)
ds2 = (2, 4, 6, 8)
ds = ds1+ds2
print(ds)
# Tạo ra một tuple mới có nội dung bằng
# dữ liệu của ds1 đúp lên 3 lần
ds1x3 = ds1*3
print(ds1x3)
 
# Tạo tuple mới bằng cách
# copy phần tử từ vị trí index đến cuối tuple
ds2 = (10, 20, 30, 40, 50, 60, 70, 30)
ds3 = ds2[4:]
print(ds3)
print(ds2[1:3])
print(ds2[:3])
# Tìm phần tử trong tuple --> True|False
kqTim1 = 40 in ds2
kqTim2 = "Bình" in danhSachTen
print(kqTim1)
print(kqTim2)
 
# Copy các phần tử của list vào tuple
list1 = ["An", "Bình", "Dũng"]
tuple1 = tuple(list1)
print(tuple1)
# Copy các phần tử của tuple vào list
list2 = list(tuple1)
print(list2)
