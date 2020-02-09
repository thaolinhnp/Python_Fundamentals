# Hàm trả về nhiều kết quả
def tong_tich(x,y):
    kqTong=x+y
    kqTich=x*y
    return kqTong,kqTich

# Tham số có giá trị mặc định
def tinh_tien_ban_hang(so_luong,don_gia,ty_gia=1):
    so_tien=so_luong*don_gia*ty_gia
    return so_tien

# Tham số tùy ý
def tinh_tong(*day_so):
    ''' Tính tổng dãy số.
        Vd: day_so:2,3,5 .Kết quả: 10
    '''
    kq=0
    for so in day_so:
        kq+=so
    return kq