import random
def KiemTraSoChan1(so):
    if so%2==0:
        print(f'{so} là số chẵn')
    else:
        print(f'{so} là số lẻ')

def KiemTraSoChan2(so):
    if so%2==0:
        return True
    else:
        return False

def KiemTraSoNguyenTo(n):
    if n<=1: return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def TongCacSoNguyenTo(lstSoNguyen):
        tongSNT=0
        for so in lstSoNguyen:
                if KiemTraSoNguyenTo(so):
                    tongSNT+=so 
        return tongSNT

def InSoNguyenTo(lstSoNguyen):
        print('\nIn các số nguyên tố')
        for so in lstSoNguyen:
                if KiemTraSoNguyenTo(so):
                        print(so,end=', ')
def DanhSachSoNguyenTo(lstSoNguyen):
        lstSNT=[]
        for so in lstSoNguyen:
                if KiemTraSoNguyenTo(so):
                        lstSNT.append(so)
        return lstSNT
def PhatSinhDanhSachSoNguyen1(sopt):
        lstKQ=[]
        for i in range(sopt): #[0,sopt)
                #soNgauNhien=random.randrange(0,101)
                soNgauNhien=random.randint(0,100)
                lstKQ.append(soNgauNhien)
        return lstKQ
def PhatSinhDanhSachSoNguyen2(lst,sopt):        
        for i in range(sopt): #[0,sopt)
                #soNgauNhien=random.randrange(0,101)
                soNgauNhien=random.randint(0,100)
                lst.append(soNgauNhien)
        