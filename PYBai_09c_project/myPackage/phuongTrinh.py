def GiaiPTB1(a,b):
    # print(f'Giải phương trình bậc 1:{a}x + {b} = 0')
    if a==0:
        if b==0:
            return ('Phương trình có vô số nghiệm')
        else:
            return ('Phương trình vô nghiệm')
    else: # a!=0
        nghiem=-b/a
        return (f'Nghiệm của phương trình là: x= {nghiem}')

def GiaiPTB1_cach2(a,b):
    # print(f'Giải phương trình bậc 1:{a}x + {b} = 0')
    if a==0:
        if b==0:
            ketQua = 'Phương trình có vô số nghiệm'
        else:
            ketQua = 'Phương trình vô nghiệm'
    else: # a!=0
        nghiem=-b/a
        ketQua = f'Nghiệm của phương trình là: x= {nghiem}'
    return ketQua

def GiaiPTB2(a,b,c):
    sup2=chr(178)
    print(f'Giải phương trình bậc 2:{a}x{sup2} + {b}y + c = 0')