lst_A=[1,3,5]
lst_B=[2,4,6]

lst_C=list(map(lambda x: x**2,lst_A))
lst_D=list(map(lambda a,b:a+b,lst_A,lst_B))

tongD1=sum(lst_D)
tongD2=sum(map(lambda a,b:a+b,lst_A,lst_B))

lst_E=list(map(str,lst_A))

print('end')