# https://www.programiz.com/python-programming/methods/list

daySo = [1, 3, 5, 7, 3, 2, 30, 10]
# A-Function:
# Tìm giá trị Max|Min

gtMax=max(daySo)
gtMin=min(daySo)

# Methods:
# Thêm phần tử
daySo.append(9)
# Chèn phần tử vào danh sách tại vị trí chỉ định
daySo.insert(1,20)
# Đếm số lần xuất hiện của một element trong list
solan = daySo.count(3)
print(solan)
# Mở rộng list
dsBS = [200, 400]
daySo.extend(dsBS)
print(daySo)

# Tìm index của element trong list
i= daySo.index(30)

# Lấy một phần tử ra khỏi list:
# kết quả trả về là phần tử
ds = ["A01", "A02", "A03", "B01", "B02"]

m = ds.pop() # Lấy phần tử cuối
print(m)
print(ds) #---> sau khi pop thì list ko còn phần tử "B02"
m1 = ds.pop(1) # Lấy phần tử tại vị trí 1
print(m1)
print(ds)
# --> pop chỉ lấy ra 1 lần 1 phần tử.
#     Nếu muốn lấy ra nhiều phần tử cùng lúc thì dùng kết hợp
#     1. Tạo list mới là các phần từ cần lấy
#     2. Del các phần tử cần lấy ở list hiện tại 

# Xóa một phần tử ra khỏi list:
# nếu ko có phần tử cần xóa sẽ thông báo lỗi. Có thể dùng Try... except... bẫy lỗi
ds = ["A01", "A02", "A03", "B01", "B02"]
ds.remove("A03") #---> remove chỉ xóa được 1 phần tử, del xóa được nhiều phần tử
ds.remove("A03")
print(ds)

# Xóa tất cả
ds.clear() #---> còn lại 1 list rỗng với 0 phần tử

# Đảo ngược giá trị các phần tử trong list
ds = [1, 2, 3, 4, 5]
ds.reverse()
print(ds)
# sắp xếp tăng
ds = [9, 2, 7, 4, 5]
ds.sort()
print(ds)
# sắp xếp giảm
ds.sort(reverse=True)
print(ds)

print('end')