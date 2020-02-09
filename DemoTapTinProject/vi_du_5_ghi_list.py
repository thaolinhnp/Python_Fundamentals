fileName=input('Tên tập tin: ')
pathAndFileName=f'Du_lieu/text/{fileName}'

lst_noiDung=['Trần Anh Thư\n','Nguyễn Thái Bình\n','Lê Anh Khoa\n']

## Ghi mới, ghi đè
f=open(pathAndFileName,'w',encoding='utf-8')
## Ghi append
# f=open(pathAndFileName,'a',encoding='utf-8')
f.writelines(lst_noiDung)
f.close()

print('Ghi thành công')