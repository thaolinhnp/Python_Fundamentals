from functools import reduce

listSo=[1,2,3,4]

tong=reduce(lambda x,y:x+y,listSo)
#Su dung buit-in function: max()
max1=reduce(max,listSo)
print(max1)
#Su dung lambda
f= lambda a,b: a if a>b else bin
max2=reduce(f,listSo)
print(max2)

#Su dung function tu viet
def timMax(a,b):
    print(f'a={a}, b= {b}')
    if a>b:
        return a
    else:
        return b

max3=reduce(timMax,listSo)
print(max3)

print('end')