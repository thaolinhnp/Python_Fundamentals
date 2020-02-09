try:
    # 1 - thu thập kết quả từ người dùng
    dtb=float(input('Nhập điểm trung bình: '))

    # 2 - xử lý tính toán
    # ketQua='Rớt'
    if dtb>=5:
        ketQua="Đậu"
    else:
        ketQua="Rớt"

    # 3 - Kết xuất - in kết quả ra màn hình

    # print('Kết quả: ',ketQua)
    # print(f'Kết quả: {ketQua}')

    str_KQ1="Điểm trung bình: " + str(dtb) + "\n" + "Kết quả: " + ketQua
    str_KQ2=f'Điểm trung bình: {dtb} \nKết quả: {ketQua}'
    print('-'*50)
    print(str_KQ2)
except ValueError:
    print('\n\t>>>>> Lỗi: Điểm phải nhập số')
print('end')