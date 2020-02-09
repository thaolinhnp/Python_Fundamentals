import os

os.mkdir('BaiTap')

thuMucHienHanh=os.getcwd()
os.rmdir("BaiTap")

os.rename('Du_lieu/text/vanban1.txt','Du_lieu/text/VB01.txt')
os.remove('Du_lieu/text/VB01.txt')

lst_Ten_tap_tin=os.listdir('Du_lieu/text')

for item in lst_Ten_tap_tin:
    print(item)

print()