'''
 - Mỗi phần tử trong set là duy nhất (Không có 2 phần tử trùng nhau) -
 - Giá trị của phần tử không thay đổi
 - Các phần tử trong set không theo thứ tự thêm vào (tự sắp xếp)
 - Không sử dụng index
'''
set1 = {1, 3, 5, 7, 2}
set2 = {"Kim", "Môc", "Thủy", "Hỏa", "Thổ"}

# Khởi tạo set rỗng

set_fruits = set()
# Cập nhật giá trị/ thêm mới phần tử vào set
set_fruits.add("orange")
# Xóa
set2.discard("Thủy") # Không ném lỗi nếu phần tử không tồn tại
# set2.remove("Thủy")  # --> Error: khi phần tử không tồn tại
# Xóa toàn bộ các element trong set
set2.clear()
# Xóa luôn set
del(set2)

set_fruits = {"apple", "pear", "orange", "grape"}
# Lấy element ra khỏi set
fruit = set_fruits.pop()

# ---len(), max(), min(), sum()
set1 = {1, 3, 5, 7, 2}
print(set1)
print("len:", len(set1))
print("max:", max(set1))
print("min:", min(set1))
print("sum:", sum(set1))
# Tạo bản sao của set
setA = {1, 3, 2}
setB = setA.copy()
print(setB)

# ------------------------------
setA = {1, 2, 6, 3, 7}
setB = {1, 4, 5, 8, 9}
# ---Union: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Lấy các tất cả các element của các set (loại bỏ trùng lắp)
setC = setA | setB
print(setC)
# --- Intersection: {1}
# Lấy các element cùng xuất hiện trong các set
setD = setA & setB
print(setD)
# Difference: {2, 3, 6, 7}
# Lấy các element chỉ có trong setA này mà không có trong setB kia
setE = setA - setB
print(setE)
# Symmetric Difference: {2, 3, 4, 5, 6, 7, 8, 9}
# trả về các element không cùng xuất hiện trong các set
setF = setA ^ setB
print(setF)

# Sắp xếp set tăng dần, giảm dần
setTen = {"Bình", "An", "Danh", "Tâm"}
print(setTen)
lstTenAsc = sorted(setTen)
lstTenDesc = sorted(setTen, reverse=True)
print(lstTenAsc)
print(lstTenDesc)

