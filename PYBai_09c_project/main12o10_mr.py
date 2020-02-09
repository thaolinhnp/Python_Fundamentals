import random
from myPackage import ThuVienHam as thuVien

if __name__ == "__main__":
    while True:
        try:
            sopt=int(input('Nhập số phần tử (số nguyên): '))  
            assert (sopt>=10),'Số phần tử phải >=10' 
            #lstSN=thuVien.PhatSinhDanhSachSoNguyen1(sopt)
            lstSN=[]
            thuVien.PhatSinhDanhSachSoNguyen2(lstSN,sopt)
            print(lstSN)
            
            thuVien.InSoNguyenTo(lstSN)            
            kqTong=thuVien.TongCacSoNguyenTo(lstSN)
            print('\nTổng giá trị các số nguyên tố:',kqTong)
            lstSNT=thuVien.DanhSachSoNguyenTo(lstSN)
            print(lstSNT)
            print(f'Tổng số NT: {len(lstSNT)}')
        except ValueError:
            print('-->>> Báo lỗi: Phải nhập số nguyên')
        except AssertionError as ThongBaoLoi:
            print(ThongBaoLoi)
        finally:
            traloi=input('\nNhấn phím bất kỳ để tiếp tục. Để kết thúc nhấn [q]: ')
            if traloi=='q': 
                break 