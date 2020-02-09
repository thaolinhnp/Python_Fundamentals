# Khởi tạo
dict1 = {1: "một", 2: "hai", 3: "ba"}
dict2 = {"một": 1, "hai": 2, "ba": 3}
dict3 = {'one': 'một', 'two': 'hai', 'three': 'ba'}
# Truy xuất, lấy value dựa trên key
k1=dict1[2]
k2=dict2['ba']

k3=dict3.get('five')  # --Không có sẽ trả về None
# k4=dict3["five"]  # --Không có sẽ báo lỗi

 
dict4 = {'x': [2, 3], 'y': (4, 1), 'z': {'s': 9, 'p': 20}}
print(dict4['x'])
print(dict4['y'])
print(dict4['z'])
print(dict4['z']['s'])
 
# Cập nhật giá trị/ thêm mới phần tử vào dictionary
dict1 = {1: "một", 2: "hai", 3: "ba"}
# Thêm mới
dict1[4] = "bốn"
print(dict1)
# Cập nhật
dict1[4] = "tư"
print(dict1)
 
# ------func & methods-----------------------------------
dict3 = {'one': 'một', 'two': 'hai', 'three': 'ba'}
# Tổng số phần tử
tongpt = len(dict3)
print(tongpt)
 
# Xóa phần tử theo khóa
del(dict3['two'])
print(dict3)
# Xóa tất cả các phần tử
dict3.clear()
print(dict3)
# Xóa luôn dictionary
del(dict3)
# print(dict3)
 
# Chuyển thành dạng chuỗi
dict3 = {'one': 'một', 'two': 'hai', 'three': 'ba'}
s = str(dict3)
print(s)
 
# Tạo bản sao của dictionary
dict3 = {'one': 'một', 'two': 'hai', 'three': 'ba'}
dictA = dict3.copy()
print(dictA)
# Kiểu dữ liệu tham chiếu
dictB = dict3
dictA['one']='1'
dictB['two']='2' #--> dict3 thay đổi theo dictB

# Tạo dictionary với danh sách các key từ sequence
listN = [1, 2, 3, 4]
dictB = dict.fromkeys(listN)
dictC = dict.fromkeys(listN, "Tháng")
print(dictB)
print(dictC)
 
# Trả về danh sách các key
dsKey = dict3.keys()
print(dict3.keys())
# Trả về danh sách các value
dsValue = dict3.values()
print(dict3.values())
 
# Cập nhật dictionary bằng cách thêm dictionary khác vào
dict1 = {1: "một", 2: "hai", 3: "ba"}
dict1BS = {4: "bốn", 5: "năm"}
dict1.update(dict1BS)
print(dict1)

# Trả về một tham chiếu đến danh sách các bộ tuple (key, value) của dictionary
dict3 = {'one': 'một', 'two': 'hai', 'three': 'ba'}
items = dict3.items()
print(items)
for key, value in dict3.items():
   print(key, ' -- ', value)
 

