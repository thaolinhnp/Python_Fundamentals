import thu_vien_ham as thuVien

if __name__ == "__main__":
    x,y=7,5
    tong,tich=thuVien.tong_tich(x,y)
    print(f'Kết quả: {x} + {y} = {tong}')
    print(f'Kết quả: {x} * {y} = {tich}')