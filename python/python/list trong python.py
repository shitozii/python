#List co the chua moi doi tuong trong python ke ca chinh no
a=[[1,2,3],'Tuan',[[['Tuan'],["Nguyen"],["Minh"]]]]
a1=[[1,2,3],[4,5,6],[7,8,9]]
b=[i for i in range(30) ]#list comprehension
c=[[n,n+1,n+2] for n in range(1,4)]#range(a,b) lay trong khoang tu a den b-1
d=list([1,2,3])
d1=list("Tuan")#chi ap dung voi iterable(tap hop gom nhieu phan tu)
print(a)
print(b)
print(c)
print(d)
print(d1)
print('Tuan' in a)#tuong tu voi cac toan tu nhan hoac cong
print(a[0])#lay cac phan tu o trong list
print(len(a))#dem phan tu
print(a[0][2])#lay 1 phan tu trong list nam trong list 
#ngoai ra cac phan lay cac phan tu trong khoang [a:b] tuong tu nhu phan chuoi
#::-1 lay toan bo phan tu nhung doa nguoc day nay
#Ta co the thay doi phan tu trong list nhung trong chuoi thi khong
a[0]="Nguyen Huu Da"
print(a)
print(a1[0])
print(a1[1])
print(a1[2])
#ban chat cua ma tran trong python la list trong list
#tuy nhien can phan biet list (co the chua nhieu kieu du lieu ) va array(chi chua mot kieu du lieu duy nhat)
'''Chu y gan hai list a=b thi tuc la dang truyen tham chieu tuc la neu ta thay doi mot gia tri phan tu phan tu cua a
thi phan tu tuong ung cua b cung bi thay doi theo.Han che gan hai list bang nhau neu khong co chu dich'''
#gan b=list(a) se khac phuc duoc tinh trang tren tuc la list a da bi copy ra mot ban sao va ta gan b voi
#ban so do nen thay doi gia tri cua b thi a ko thay doi
#bai tap giai thich
'''
Cho chuoi code
a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
b[0][0]='Tuan'
Ket qua in ra ca phan tu dau tien cua list dau tien trong ca a va b deu thay doi giai thich.Tim cach thay doi
'''