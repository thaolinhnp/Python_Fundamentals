hoTen=str(input('Nhập họ tên: '))

i=hoTen.find(' ')
j=hoTen.rfind(' ')

ho=hoTen[:i]
ten=hoTen[j+1:]
tenLot=hoTen[i+1:j]

print("Họ:",ho)
print("Tên lót:",tenLot)
print("Tên:",ten)
print('end')