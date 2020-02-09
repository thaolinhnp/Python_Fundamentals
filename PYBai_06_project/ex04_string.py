# s1='   trung tÂm tin học   '
# k1=s1.capitalize() #--> '   trung tâm tin học   '

# k2=s1.upper() #--> '   TRUNG TÂM TIN HỌC   '
# k3=s1.lower() #--> '   trung tâm tin học   '
# k4=s1.title() #--> '   Trung Tâm Tin Học   '

# k5=s1.strip() #--> 'trung tÂm tin học'
# s2='20,30,'
# k6=s2.strip(',') #--> '20,30'

# s3='Xin chào "Hùng"!'
# print(s3)

# s4="Xin chào \"Hùng\"!"
# print(s4)

# baiTho="""
# Chiều trời bảng lảng bóng hoàng hôn,
# Tiếng ốc xa đưa lẩn trống đồn.
# Gác mái, ngư ông về viễn phố,
# Gõ sừng, mục tử lại cô thôn.
# Ngàn mai gió cuốn chim bay mỏi,
# Dặm liễu sương sa khách bước dồn.
# Kẻ chốn trang đài, người lữ thứ,
# Lấy ai mà kể nỗi hàn ôn?
# """

# tieuDe="Buổi chiều lữ thứ"
# print("*"*37)
# print(tieuDe.center(37,"*"))
# print(baiTho)
# print("*"*37)

# k7=baiTho.count('cảnh') #--> 3
# k8=baiTho.count('cảnh',0,100) #--> 1

# k9=baiTho.find('cảnh') #--> 50
# k10=baiTho.find('Cảnh') #--> Tìm không thấy: -1

# hoTen="Trần Lê Anh Thư"
# i=hoTen.find(' ') #--> 4
# j=hoTen.rfind(' ') #--> 8

# s5="123456"
# kq1=s5.isdigit() #--> True
# s6="abc"
# s7="123vnd"
# s8="123.20"
# s9='ASD'
# kq2=s6.isalpha()
# kq3=s7.isalpha()
# kq4=s8.isdecimal()
# kq5=s6.islower() 
# kq6=s9.isupper()

soTien=12000000.25
str_soTien1='{:,}VND'.format(soTien)
# str_soTien2=str_soTien1.replace(',','.')

str_soTien3='{:>10}'.format(soTien)

str1=str_soTien1.rjust(40,'*')
str2=str_soTien1.ljust(40,'*')

print('end')