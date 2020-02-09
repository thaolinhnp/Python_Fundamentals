import random
from myPackage import ThuVienHam as thuVien

if __name__ == "__main__":
    while True:
        try:
            sopt=int(input('Nhập số phần tử (số nguyên): '))   
            assert (sopt>=10),'Số phần tử phải >=10'
            lstSN=[]
            for i in range(sopt): #[0,sopt)
                #soNgauNhien=random.randrange(0,101)
                soNgauNhien=random.randint(0,100)
                lstSN.append(soNgauNhien)
            print(lstSN)
            #Tính tổng số nguyên tố
            tongSNT=0
            for so in lstSN:
                if thuVien.KiemTraSoNguyenTo(so)==True:
                    tongSNT+=so 
                    #tongSNT=tongSNT+so
            print('Tổng số nguyên tố là: ',tongSNT)
        except ValueError:
            print('-->>> Báo lỗi: Phải nhập số nguyên')
        except AssertionError as ThongBaoLoi:
            print(ThongBaoLoi)
        finally:
            traloi=input('Nhấn phím bất kỳ để tiếp tục. Để kết thúc nhấn [q]: ')
            if traloi=='q': 
                break 