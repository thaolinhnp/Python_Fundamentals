import random
# phát sinh một số (thực) ngẫu nhiên [0,1)
n1=random.random()
print(n1)

# phát sinh một số nguyên ngẫu nhiên từ 10 đến 15 với step=1
n2=random.randrange(10,16)
print(n2)

n3=random.randrange(10,16,1)
print(n3)

# phát sinh một số nguyên ngẫu nhiên từ 10 đến 15
n4=random.randint(10,15)