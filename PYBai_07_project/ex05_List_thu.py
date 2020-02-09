from datetime import datetime

# Nhập ngày sinh -> sinh vào thứ mấy
str_NgaySinh = input('Nhập ngày sinh (dd-mm-yyyy):')
NgaySinh = datetime.strptime(str_NgaySinh,"%d-%m-%Y")
stt_thu = NgaySinh.weekday()
dsThu = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ Nhật"]
thu_NgaySinh = dsThu[stt_thu]
print(f'Sinh nhật bạn là ngày thứ: {thu_NgaySinh}')