#Bai 1
a= 10
b= 10.0
from decimal import*
getcontext().prec=9
c=Decimal(10)/3 #ep mot trong 2 bien la kieu decimal nhung khong duoc cho no vao ca phep tinh
print(c)
d=5+1j#bt buoc phai ghi ca phan ao cho du la 0 hay 1
d1=6+5j
print(d.real)
print(d.imag)
print(5**3)

import math 
print(math.fabs(-11.5))
print(math.trunc(10/-3))
#Bai 2
#Chuoi tran
print(r'Nguyen Minh Tuan \n \a Tran Thi \t')
e='Nguyen Minh Tuan'
print(e)
e=e.replace('n','t',1)#ham replace tra ve kieu chuoi no khong phai la phuong thuc nen neu khong gan thi ko thay doi
print(e.replace('n','t',2))
print(len(e))
print(e[:])
print(e[3:8])
g='Ten toi la %s .Toi nam nay %d tuoi' %('Nguyen Minh Tuan',19)
print(g)
print('%.2f'%(4.336))
name='Tuan'
ID='20194876'
h=f'Ten toi la {name} .MSSSV cua toi la {ID}'
h1='Ten toi la {}.MSSV cua toi la {}'.format('Tuan',20194876)#khong ap dung format voi chuoi f-string
print(h)
print(h1)
i="How to train My Dragon"
print(i.capitalize())
print(i.upper())
print(i.lower())
print(i.swapcase())
print(i.title())
print('Dragon'.center(10,'*'))
print('Dragon {:^10}'.format('*'))
print('Dragon'.rjust(10,'-'))
print('Dragon'.ljust(10,'='))
print('Dragon'.encode())
print('Dragon'.join(['1','2','3']))
print('Dragon'.strip('D'))
print(i.split(' ',2))
print('Dragon is life'.partition('i'))
print('Dragon no nail'.count('n'))
print('Dragon'.find('o'))
#Bai 3:
l1=[1,2,[3,4]]
print(l1)
l2=[n for n in range(10)]
print(l2)
l3=list()
print(l3)
print(len(l1))
l4=[[1,2,3],[4,5,6],[7,8,9]]
print("%d,%s,%d"%(l4[0][0],l4[1][1],l4[2][2]))
print(l1+l2)
print(l1*3)
l5= [1,2,5,8,6,9,8,3,4,7,10]
print(len(l5))
print(l5.index(8))
print(l5.copy())
l5.insert((l5.index(3)+1),12)
print(l5)
l5.extend([13,14,15])
print(l5)
print(l5.pop(12))
l5.reverse()
print(l5)
l5.sort(reverse=True)
print(l5)
#Bai 4:
t1=(n for n in range(20) if n%2==1)
print(next(t1))
t2=tuple(t1)
print(t2)
print(t2[::-1])
#Bai 5
set1=set()
set1={1,2,3,4,5}
set2={3,4,6}
print(set1^set2)#chi ton tai o mot trong hai set 
print(set1&set2)
print(set1|set2)
print(set1-set2)
#Bai 6:
dic1={(9,10):'Nguyen Minh Tuan','Honey':'Mat ong'}
print(dic1)
dict2={}
dict3={keys:values for keys,values in [('Tuan','Dep trai'),('Hieu',"Thong minh")]}
print(dict3)
iter_=[('Tuan','DC'),('Dep trai',100)]
dict4=dict(iter_)
print(dict4)
itera2=('Tuan','DC')
dict5=dict.fromkeys(itera2,10)
print(dict5)
dict5['Hochanh']='Cham chi'
print(dict5)
dict6=dict(x='Deptrai',y='Ngu nguoi')
print(dict6)
print(dict6.copy())
print(list(dict6.items()))
print(dict6.get('x'))
print(list(dict6.values()))
print(list(dict6.keys()))
dict6.setdefault('DC',12)
print(dict6)
print(dict6.pop('DC'))
print(dict6)
p=[('a','chu a'),('b','chu b')]
dict6.update(p)
print(dict6)
dict6.update(x='Hansome')
print(dict6)
#Bai7:Doc ghi file
file_object=open('file1.txt')#mode='...'/a a+
data=file_object.read(10)#chu y ta phai dua read den bien khac neu khong file object bi gan la str
print(data)
file_object.close()
file_object=open('file1.txt')
data=file_object.readline()
print(data)
data=file_object.readline()
print(data)
file_object.seek(0)
print(file_object.readline())
file_object.close()
file_object=open('file1.txt')
data=file_object.readlines()
print(data)
file_object.close()
file_object=open('file1.txt',mode='a')
data=file_object.write(' 10 diem')
print(data)
file_object.close()
with open('file1.txt') as fobj:
 data=fobj.read()
 print(data)
#Bai 8:
print(sum((1,2,3)))
print(min(1,2,3))
print(max(1,2,3))
print(sorted((2,4,5,4,7),reverse=True))