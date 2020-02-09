namDL=int(input('Nhập năm dương lịch: '))

csCan=namDL % 10
csChi=namDL % 12
tuple_can=('Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ')
tuple_chi=('Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi')

namAL=tuple_can[csCan] + ' ' + tuple_chi[csChi]

print('Năm âm lịch là: ', namAL)