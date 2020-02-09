from myPackage import phuongTrinh

if __name__ == "__main__":
    a=int(input('Nhập hệ số a:'))
    b=int(input('Nhập hệ số b:'))
    kq=phuongTrinh.GiaiPTB1(a,b)
    print(f'Giải phương trình bậc 1:{a}x + {b} = 0')
    print(f'Kết quả: {kq}')