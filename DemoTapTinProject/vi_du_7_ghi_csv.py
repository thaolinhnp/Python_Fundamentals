import csv

pathAndFileName='Du_lieu/csv/DSHVK251.csv'
f=open(pathAndFileName,'w',encoding='utf-8')

lst_HV=[['Tam','tam@gmail.com'],['Thanh','thanh@gmail.com']]

for item in lst_HV:
    csv.writer(f).writerow(item)

f.close
print('')