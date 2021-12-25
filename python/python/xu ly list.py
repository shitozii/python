a=[1,1,1,3,4,5,7,6,10,10]
b=[n for n in range(20)]
c=[1,2,2,3]
a1=[5,3,9,7,5,4]
print(a.count(1))#count in ra so luong phan tu xuat hien trongl list
print(a.index(4))#in ra vi tri dau tien uat hien phan tu can truy xuat ,bao loi neu phan tu khong co trong list
print(a.copy())#tao ra ban sao cua a khi gan c=a.copy() thi phan thi thay doi c a se khong doi
#d=c.clear()#giai thich sau tai sao print d lai ra none ?
#boi vi chung ta khong the gan mot bien voi mot phuong thuc nhu clear ,append hay extend.
#phai khia bao truoc khi print
#phuong thuc o day co the coi la mot ham kieu void trong c tuc la no chi thuc hien chuc nang chu 
#khong tra ve mot gia tri nhat dinh de ta co the gan 
a.append([4,5])
print(a)
a.extend([4,5,[7,8]])#lay tung phan tu ngan cach nhau boi dau phay
print(a)
a.insert(2,3)#insert(a,b) them phan tu b vao vi tri 2
print(a)
k=c.pop(0)#phuong thuc pop(a) loai bo phan tu thu a cua chuoi va tra ve phan tu thu a day
print(c)
print(k)
c.remove(2)#bo di phan tu dau tien co gia tri 2(void),bao loi neu phan tu x khong co trong list
print(c)
b.reverse()#dao nguoc day
print(b)
a1.sort()#sap xep day theo thu tu tang dan
print(a1)
a1.sort(reverse=True)#sap xep theo thu tu giam dan
print(a1)
