def tinh_tong(x,y):
    ''' Tính tổng 2 số nguyên '''
    ket_qua=x+y
    return ket_qua

def tinh_tich(x,y):
    ket_qua=x*y
    print('ket qua:',ket_qua)

#-----------------------------------------------
# code xử lý của chương trình chính
# test funtion

# Trường hợp 1:
# print ('--main 01--')
# kq=tinh_tong(3,5)
# print('kết quả tổng:',kq)
# tinh_tich(3,5)
# print('--end main 01--')

# Trường hợp 2:
if __name__ == "__main__":
    kq=tinh_tong(3,5)
    print('ket qua tổng 1:', kq)
    tinh_tich(3,5)