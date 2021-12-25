#toan tu cua chuoi giong toan tu cua tuple nhung toan tu cua list chi "gan giong" toan tu cua chuoi
tup=(1,) # phan biet tuple 1 phan tu voi gia tri
tup1=(i for i in range (20) if i%2==0)
#neu in truc tiep tup1 ra se bao loi vi khai niem comprehension khong dc ap dung .bat buoc phai thong qua constructor
print(tup)
a1=tuple(tup1)#generator expression
a=tuple('Tuan')#constructor
a2=1 in tup
#cau truc dao chuoi va list a=tup[::-1] 
#tuple -khong the thay doi gia tri cua tup
print(a)
print(a1)
print(a2)
#-----------------------------
#hashable va unhashable
a=id(5)#trong c tuong tu dia chi 
print(a)
#+= la phuong thuc nen khi ap dung voi mot unhashable object thi id se khong doi
#s_1=s_1+[3,4] ta da gan lai gia tri cua s_1 nen mac nien no se bi dua den mot dia chi khac'  