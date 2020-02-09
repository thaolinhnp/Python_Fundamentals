import random
# Viết CT cho in ra n số nguyên trong khoảng từ 10 đến 20
n = int(input("Nhập n = "))

# for i in range(n):
#     r = random.randrange(10,20)
#     print(r, end=', ')

chuoi = ''
tong = 0
for i in range(n):
    r = random.randint(10,20)
    chuoi = chuoi + ', ' + str(r)
    tong += r

print(chuoi[1:])
print('Tổng:',tong)
