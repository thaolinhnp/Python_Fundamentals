lst_N=[2,3,15,6,5,10]

laBoiSoCua5= lambda n: True if n%5==0 else False
lst_BS5=list(filter(laBoiSoCua5,lst_N))

lst_BS3=tuple(filter(lambda n: True if n%3==0 else False,lst_N))

def laBoiSoCua3va5(n):
    if n%3==0 and n%5==0:
        return True
    else:
        return False

set_BS35=set(filter(laBoiSoCua5,lst_N))

print('end')