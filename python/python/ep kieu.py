'''print("Nhap USD")
usd=input()
vnd=22*int(usd)
print(type(usd))
print(str(usd)+"USD="+str(vnd)+"kVND")
int chi co the bien chuoi so nguyen thanh so nguyen con float moi co ythe bien so thuc tanh so thuc
Tim hieu ve mutable and immutable object'''
strA="NguyenNguyenNguyen"
#strA=strA[None:1]+"G"+strA[2:None]
strA=strA.replace("Ng","Q",1)
#cau truc ham replace str.replace("chuoi con can thay the","chuoi thay the",so ky tu tuong duong can thay the tinh tu trai qua phai)
#hoc them cac ham xu ly chuoi trong python va ham hash
print(strA)
#strB="10"
#print(hash(strB))
'''Phan biet %s va %r :%s la thay the cho phuong thuc _str_ tao nen doi tuong do,
%s va %r co the ap dung voi moi doi tuong trong python
'''
a= "My name is %s .I'm %d years old "%("Tuan",int(19))
b= "%.2f"%(4.55879)
print(a)
print(b)
#Chuoi f-string
name='Tuan'
ID='20194876'
Phone='074374839554'
result=f'Student:{name}\nStudentID :{ID}\nPhone:{Phone}'
print(result)
#Dinh dang kieu format
a1='a:{},b:{},c:{}'.format('one','two','three')
#a1='a:{1},b:{2},c:{2}'.format('one','two','three')
#co the gan a:{one} b:{two}.format('1','2')
print(a1)
#can le 
cc='Nguyen {:^10} Tuan '.format('Minh')
ll='Nguyen {:<10} Tuan'.format('Minh')
rr='Nguyen {:>10} Tuan'.format('Minh')

print(cc)
print(ll)
print(rr)
#BAI TAP KE BANG