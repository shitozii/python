print('how to train My Dragon'.capitalize())
print('How to train My Dragon'.upper())
print('How to train My Dragon'.lower())
print('How to train My Dragon'.swapcase())
print('How to train My Dragon'.title())
print('Dragon'.center(10,'*')) #chi ap dung cho 1 tu hay 1 chuoi lien tuc khong co khoang trang
print('Dragon'.rjust(10,'-'))
print('Dragon'.ljust(10,'='))
print('Dragon'.encode())
print('Dragon'.join(['12','2','3']))
print('Dragon'.strip('D'))
#loai bo ky tu o hai dau ,neu co khoang trang thi loai khoang trang 
#ngoai ra con co rstrip va lstrip
a="How to train My Dragon"
b=a.split(' ',2)#Dau trong split chinh la delimeter
#ngoai ra con co rsplit
print(b)
print('Dragon is life'.partition('i'))
print('Dragon is life'.count('i'))
print('Dragon is life'.count('i',0,9))
print('Dragon is life'.startswith('D'))
print('Dragon is life'.startswith('i',7))
#ngoai ra con co endswith
print('Dragon is life love'.find('love'))#xuat ra vi tri dau tien chu i xuat hien
#rfind in ra vi tri dau tien chu i uat hien tinh tu ben trai
#ngoai ra con co cac ham tuong tu nhu c nhu isdigit isspace,.... tu tim hieuB



