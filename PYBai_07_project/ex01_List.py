# Khởi tạo list
daySo = [200, 10, 30, 100]
danhSachTen = ["Tâm", "Thanh", "Bình"]
danhSach = [9, 'abc', True]

# In danh sách
print(danhSachTen)

# Tổng số phần tử
tongspt = len(daySo)
print('Tổng số phần tử:', tongspt)

# Truy xuất giá trị phần tử
print(daySo[0])
print(danhSachTen[1])
print(danhSachTen[-1])

# Thay đổi giá trị phần tử
danhSachTen[1] = "Phúc"

# Xóa phần tử trong list khi biết chỉ số index
del(daySo[2])
# deleta multiple items
daySo = [100, 200, 300, 400, 500, 600, 700]
del daySo[1:5] #--> xóa phần tử từ 1 đến 4. Kết quả = [100, 600, 700]

# Ghép dữ liệu các list --> tạo ra list mới
ds1 = [1, 3, 5]
ds2 = [2, 4, 6, 8]
ds = ds1+ds2
print(ds)
# Tạo ra một danh sách mới có nội dung bằng
# dữ liệu của ds1 đúp lên 3 lần
ds1x3 = ds1*3
print(ds1x3)

# Tạo ra list mới bằng cách
# copy phần tử từ vị trí index đến cuối list
ds2 = [10, 20, 30, 40, 50, 60, 70, 30]
ds2New = ds2[4:]
print(ds2New)

# Tìm phần tử trong list --> True|False
kqTim1 = 40 in ds2
kqTim2 = "Bình" in danhSachTen
print(kqTim1)
print(kqTim2)