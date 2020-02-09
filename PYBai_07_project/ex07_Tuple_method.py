daySo = (1, 3, 5, 7, 3, 2, 30, 10)
# A-Function:
# Tìm giá trị Max|Min
 
print('Max=', max(daySo))
print('Min=', min(daySo))
 
# --- Methods:
 
# Đếm số lần xuất hiện của một element trong tuple
solan = daySo.count(3)
print(solan)
 
# --Trong tuple có tuple và list
tuple1 = ('a', ('a', 'b'), ('a', 'b'), [3, 4])
 
# --- Đếm element ('a', 'b')
d1 = tuple1.count(('a', 'b'))
print("d1=", d1)
 
# --- Đếm element [3, 4]
d2 = tuple1.count([3, 4])
print("d2=", d2)
 
 
# Tìm index của element trong tuple
i = daySo.index(3)
print(i)
k1 = tuple1.index(('a', 'b'))
print("k1=", k1)
 
k2 = tuple1.index([3, 4])
print("k2=", k2)
 
# https://www.programiz.com/python-programming/methods/built-in/sorted
tupleN = (3, 1, 4, 2)
tupleAsc = sorted(tupleN)
tupleDesc = sorted(tupleN, reverse=True)
print(tupleAsc)
print(tupleDesc)
 
# del tuple
tupleD = (1, 12, 3)
del(tupleD)
# print(tupleD)  # NameError: name 'tupleD' is not defined
 
# sum
tupleM = (1, 3, 5)
tong1 = sum(tupleM)
print('tong1=', tong1)

