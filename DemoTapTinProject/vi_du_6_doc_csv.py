import csv

pathAndFileName='Du_lieu/csv/dienthoai.csv'
f=open(pathAndFileName,'r',encoding='utf-8')

# #Cách 1:
# lst_KH=[]
# for dong in csv.reader(f):
#     lst_KH.append(dong)
#     print(dong)
# f.close()

# #Cách 2: sử dụng list comprehension
lst_KH=[dong for dong in csv.reader(f)]

print('')