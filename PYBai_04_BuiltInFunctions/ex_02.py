try:
    # 1 - thu thập kết quả từ người dùng
    dtb=float(input('Nhập điểm trung bình: '))
    # 2 - kiểm tra miền giá trị
    if dtb>=0 and dtb<=10:
        # 3 - Điểm hợp lệ: xét xếp loại (xử lý tính toán)
        xepLoai=''
        if dtb>=9:
            xepLoai='Xuất sắc'
        elif dtb>=8:
            xepLoai='Giỏi'
        elif dtb>=7:
            xepLoai='Khá'
        elif dtb>=6:
            xepLoai='Trung bình khá'
        elif dtb>=5:
            xepLoai='Trung bình'
        else:
            xepLoai='Yếu'
        # 4 - Kết xuất
        print(xepLoai)
    else:
        # Điểm không hợp lệ: xuất thông báo lỗi
        print('-->>> Lỗi: Điểm không hợp lệ. Phải từ 0 đến 10')

    # 3 - Kết xuất - in kết quả ra màn hình
    print(xepLoai)
except ValueError:
    print('\n\t>>>>> Lỗi: Điểm phải nhập số')
print('end')