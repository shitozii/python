#Bai 1
import math 
print(math.trunc(15/-4))
print(15//-4)
print(type(math.fabs(-4)))
'''Ham trunc lay phan nguyen cua so thuc con toan tu // lay ket qua
 la so nguyen nhung phai nho hon hoac bang ket qua cua phep chia'''
#Bai 2
#Mot string bat dau bang " hoac ' va ket thuc bang dau tuong ung voi no tu la ta 
#khong thhe dua cac ky tu nay vao trong chuoi tuong ung voi dau mo dau va ket thuc chuoi
print("\\n")#ky tu \bien dau \ thnh dau \
print("39\43ni")#chu y \+1 so se ra cac ky tu khac ex \5 dau + \4 la dau thang 
print("\/\/\/\\/\/")
#Bai 3
#Chuoi tran su dung chu yeu trong Regular Expression
#ham in khong giup chuyen doi so thuc ma chi co ham float
c='tuan'
print(c[0:0:-1])#hai gia tri dau trung nhau in ra chuoi rong
#Bai 4:
c1='aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
print(((((c1.lstrip('aoA'))).rstrip('a'))).title())
#Bai 5
#contrutor list(iterable object)
s='aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
print(((s.split('&&'))[1].split('%%'))[0])
#phuong thuc 
tup = 1,2#unpacking argument
print(type(tup))
#Huong dan sau mapping object
#packing va unpacking arg


