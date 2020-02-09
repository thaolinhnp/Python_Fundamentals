fileName=input('Nhập tên tập tin: ')
pathAndFileName=f'Du_lieu/text/{fileName}'

# f=open(pathAndFileName)
f=open(pathAndFileName,'r',encoding='utf-8')
noiDung=f.read()
# f.close
print(noiDung)

viTriHienHanh=f.tell()
noiDung6=f.read(6)
f.seek(10,0)
viTriHienHanh=f.tell()
noiDung6=f.read(6)



print('end')