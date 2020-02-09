import thu_vien_ham as thuVien

if __name__ == "__main__":
    soTien1=thuVien.tinh_tien_ban_hang(2,15000)
    # Truyền giá trị cho tham số theo định danh (Keyword arguments)
    soTien2=thuVien.tinh_tien_ban_hang(don_gia=15000,so_luong=2)
    soTien3=thuVien.tinh_tien_ban_hang(2,100,20000)
    print('Số tiền 1:',soTien1)
    print('Số tiền 2:',soTien2)