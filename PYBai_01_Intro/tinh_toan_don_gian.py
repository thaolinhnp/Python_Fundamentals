x=float(input('x ='))
y=float(input('y ='))

tong=x+y
tich=x*y
hieu=x-y
thuong=x/y

print('X=',x,', Y=',y)
print('Tổng x+y= ',tong)
print('Tích x*y= ',tich)
print('Hiệu %d - %d = %d' %(x,y,hieu))  #so nguyen %d hoac %i
print('Thương %f - %f = %f' %(x,y,thuong)) #so thuc f
print('Thương %.2f - %.2f = %.2f' %(x,y,thuong)) #so thuc lay 2 chu so 0 sau , f