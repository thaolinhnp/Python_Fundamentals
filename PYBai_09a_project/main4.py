# Global variable - Biến toàn cục
tenHocSinh="An"

def InThongTin1():
    print(f'1-Tên HS (Global variable):{tenHocSinh}')

def InThongTin2():
    # Local variable - Biến cục bộ trong function
    hoHocSinh='Lê'
    tenHocSinh='Bình' 
    print(f'2-Tên HS (Local variable):{hoHocSinh} {tenHocSinh}')

def InThongTin3():
    # Global variable - Biến toàn cục
    global hoHocSinh
    hoHocSinh='Lê'
    global tenHocSinh
    tenHocSinh='Bình' 
    print(f'3-Tên HS (Global variable):{hoHocSinh} {tenHocSinh}')

if __name__ == "__main__":
    # InThongTin1()
    # InThongTin2()
    # print(f'Main - Tên HS (Global variable):{tenHocSinh}')
    InThongTin3()
    print(f'Main-Tên HS (Global variable):{hoHocSinh} {tenHocSinh}')

    print('end')