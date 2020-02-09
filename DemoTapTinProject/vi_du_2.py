pathAndFileName='Du_lieu/text/ConGapNhau.txt'

f=open(pathAndFileName,'r',encoding='utf-8')
## In toàn bộ số dòng của bài thơ
# d=0
# for dong in f:
#     print(dong)
#     d+=1
# f.close()
# print('\nSố dòng',d)

## In toàn bộ 6 dòng đầu của bài thơ
# d=0
# for dong in f:
#     print(dong)
#     d+=1
#     if d == 6:
#         break
# f.close()
# print('\nSố dòng',d)

## Xóa khoảng trắng giữa dòng của bài thơ
# d=0
# for dong in f:
#     print(dong,end='')
#     if dong!="\n":d+=1
# f.close()
# print('\nSố dòng',d)

## Đếm số chữ trong bài thơ
d=0
demTu=0
for dong in f:
    print(dong,end='')
    if dong!="\n":d+=1
    
    lst_Tu=dong.split()
    demTu+=len(lst_Tu)
f.close()
print('\nSố dòng',d)
print('\nSố từ',demTu)