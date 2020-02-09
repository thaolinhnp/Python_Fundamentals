fileName=input('Tên tập tin: ')
pathAndFileName=f'Du_lieu/text/{fileName}'

noiDung=input('Nội dung:\n')

## Ghi mới, ghi đè
# f=open(pathAndFileName,'w',encoding='utf-8')
## Ghi append
f=open(pathAndFileName,'a',encoding='utf-8')
f.write(noiDung)
f.close()

print('Ghi thành công')