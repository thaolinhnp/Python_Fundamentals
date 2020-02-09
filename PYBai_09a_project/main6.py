
def tinhTich(x,y):
    x=x+2 # Làm thay đổi giá trị của tham số hình thức
    return x*y

def ThemHocSinh(lstHocSinh):
    lstHocSinh.append('Hạnh')

if __name__ == "__main__":
    # Tham số thực
    # a=5
    # b=7
    # kqTich=tinhTich(a,b)
    # print(f'a={a}, b={b}, tich={kqTich}')

    lstHS=['An','Bình']
    ThemHocSinh(lstHS)
    
    print('end')