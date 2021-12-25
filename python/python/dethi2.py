from time import sleep
import os
from functools import reduce 
import math
###XU ly text \
#BAI 1
'''value=input('Nhap cac so')
lst=value.split(',')
tup=tuple(lst)
print(lst)
print(tup)'''
#Bai 2
'''value=input("Nhap vao cac tu cach nhau boi dau phay:  ")
lst=value.split(",")
print(sorted(lst))'''
#Bai 3
'''print(" ".join(sorted(set((input("Nhap vao cac tu ")).split(' ')))))'''
#Bai 4
'''chuoi=input("Nhap vao chuoi cua ban ")
countnum=0
countc=0
for x in chuoi:
	if(x.isdigit()):
		countnum+=1
	if(x.isalpha()):
		countc+=1
print(countnum)
print(countc)	'''
###Xu ly chuoi print
#print("Kteam"+str(69))<=>print("Kteam",69,sep='')
#value=1,2,3 #packing argument
#so di ham print khong can biet so luong di vao nhung no van
#in ra dc het tat cac cac phan tu boi vi no goi tat cac cac argument
#thanh 1 tuple
'''with open("Tuan.txt","w") as fobj:
	print("Tuan dep trai",file=fobj)'''
'''for x in "Tuan dep trai":
	print(x,end='')
	sleep(0.2)'''
'''print('start...',end='',flush=True)
sleep(3) # dừng chương trình 3 giây
print('end...')'''
#Ham input co cau truc input(prompt=None) prompt la positional argument
#------------------------------------------------------
#De quy
#Bai 1
'''def dequy(n):
	if(n==0):
		return 1
	if(n==1):
	    return 1
	else:
		return dequy(n-1)+dequy(n-2)
sum=0		
for x in range(6):
	sum+=dequy(x)
print(sum)'''
#Giai thuat thap hanoi
'''def dequy(n,a,b,c):
	if(n==1):
		print(a,c,sep='-----')
	else:
		dequy(n-1,a,c,b)
		dequy(1,a,b,c)
		dequy(n-1,b,a,c)

dequy(2,'A','B','C')'''
#default arg phai khhai bao o cuoi
#default arg la mot unhashable container
'''def tuan(tuan1=[]):
    tuan1.append('A+')
    print(tuan1)	
tuan()
tuan()
tuan()'''
#co the truyen theo ca kieu positional va keyword nhung positionla phai truoc key word
'''def tuan(a,b,c):
	pass
tuan(a=1,2,c=3)''' #vi du nay se bao loi vi positional o sau 1 keyword
#ham sorted la ham bat buoc phai su dung keyword only argument vd reverse=True
#ky tu sao phan tach  positional arg va only keyword arg
'''def tuan(a,b,*,c=2,d=4):
	pass
tuan(1,2,d=3,c=4)'''#truyen theo kieu keyword ko nhat thiet phai theo thu tu
'''lst=[1,2,3,4]
def tuan(m,i,n,h=5):
    pass
tuan(*lst)'''#unack va truyen theo kieu positional vao tung parameter
#unpack duoc ca chuoi ca tuple,neu co keyword only thi ko truyen dc
'''def tuan(*arg,tun): # parameter kieu sao goi cac arg dc truyen vao thanh 1 tuple
	print(arg)
tuan(69,"MinhTun",tun=10)'''#packing patameter la 1 cai ko phai thi phai truyen thoe kieu
#keyword va ko dc phep co 2 parameter cung lam nhiem vu pack
#thong thuong bien packing nen dat ten la args
#mot the manh cua python la no co the so sanh truc tiep cac iterable vs nhau
#toan tu is so anh 2 id nen khi gan 2 list bang nhau toan tu is tra ve true
#tuy nhien voi cac so trong khoang -5 den 256 va chuoi co duoi 20 ky tu lai tra ve cung 1 id
'''def kteam(Tuan,DC):
	print(Tuan)
	print(DC)
dic={'Tuan':'Dep trai','DC':'Thong minh'}
kteam(**dic)#phai gan theo keyword'''
'''def kteam(**kwargs):
	print(kwargs)
kteam(Tuan="Deptrai",Kteam="ngu si")''' 
'''print(locals())
print(globals())'''
#Dang return khong co gi phia sau la return none
'''def kteam(a,b):
	tuan=10*a
	DC=9*b
	return tuan,DC 
print(type(kteam(10,9)))#=> return 2 gia tri tra ve 1 tuple
c,d=kteam(10,9)
print(c)
print(d)'''
'''lst=[(-5,-20),(-4,-15),(-3,4),(-2,9),(-1,7),(0,1),(1,-7),(2,-9),(4,81),(5,130)]
def f(x):
	 return x**3+2*(x**2)-4*x+1
def check(x,y):
	if(y==f(x)):
		return True
	return False	
def kiemtra(lst):
	lst_A=[]
	lst_B=[]
	for x in lst:
		if(check(*x)==True):
			lst_A.append(x)
		else:
		    lst_B.append(x)
	return lst_A,lst_B	    
lstA,lstB=kiemtra(lst)
def sum(lst):
	sum=0
	for x in lst:
		sum+=x[1]
	return sum
print(sum(lstA))
print(sum(lstB))	'''
'''def find_max(a,b):
	if a>b:
		return a
	return b
a=32
b=59
c=8
d=24
e=15
print(find_max((find_max((find_max((find_max(a,b)),c)),d)),e))'''
'''def kteam():
	for value in range(3):
		print("Hello %d"%value)
		yield value
for value in kteam():
	print(value)'''
'''def square(lst):
	yield lst[0]
	yield lst[1]
for value in square([1,2,3]):
	print(value)'''
'''def gen():
	for i in range(4):
		x=yield i
		print(type(x))
g=gen()
print(next(g))
g.send("Tuan")		
print(next(g))
print(next(g))
print(next(g))'''
'''a=lambda x,y:x+y
print(a(1,2))	
b=lambda x :x**2
print(b(5))
def callmyname():
	return lambda x:"Hello"+x
k=callmyname()
print(k(" Tuan"))	
dic={'Tuan':lambda :"Dep trai","DC": lambda:"Stupid"}
print(dic['Tuan']())'''
'''b=lambda x:(True if 9%x==0 else False) if 15%x==0 else False
print(b(3))'''
'''def f(x):
	return x*x
a=map(f,[1,2,3,4])#ham map tra ve map object(generator) vi no co phuong thuc yield
print(a)
print(next(a))'''
'''a=lambda x,y:x+y
lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=list(map(a,lst1,lst2))
print(lst3)'''
'''func=lambda x:x%2==0
lst=list(filter(func,[1,2,3,4,5,6,7,8,9,10]))
print(lst)'''
#neu ham la NOne filter tra ve cac gia tri khac 0,False hoac None
'''a=lambda x,y:x if x>y else y
print(reduce(a,[1,4,6,8,3,10,9,5,4,4]))'''
#BAI 1: Chu y phuong thuc join chi chap nhan cac iterable co cac phan tu o dang chuoi
'''lst=[]
for x in range(2000,3201):
	if x%7==0 and x%5!=0:
		lst.append(str(x))
print(",".join(lst))'''
#BAI 2
'''dic={}
for i in range(1,9):
	dic[i]=i**2
print(dic)'''
#Bai 9
'''def func(x,c=50,h=30): 
	return int(math.sqrt((2*c*x)/h))
str1="100,150,180"#chu y ghi nho cach kinh dien lst=(x for x in input("NHap cac gia tri").split(","))
lst=str1.split(",")
lst1=[]
for x in lst:
	lst1.append(str(func(int(x))))
print(','.join(lst1))'''
#Bai 10
'''i=3
j=5
lst=[[0 for x in range(5)] for x in range(3)]
for x in range(i):
	for y in range(j):
		lst[x][y]=x*y
print(lst)	'''	
#Bai 15
'''def kiemtra(x):
	while(x>0):
		m=x%10
		x=int(x/10)
		if(m%2==1):
			return False
	return True
lst=[]
for x in range(1000,3001):
    if(kiemtra(x)==True):
        lst.append(str(x))
print(" ".join(lst)) ''' #ham while se khien cho code chay cham
#=>huong tiep can don gian hon
'''lst=[]
for x in range(1000,3001):
    str_=str(x)
    if int(str_[0])%2==0 and  int(str_[1])%2==0 and  int(str_[2])%2==0 and  int(str_[3])%2==0  :
        lst.append(str_) 	
print(" ".join(lst))  '''
'''import re
items=['ABd1234@1','aF1,2w3E#','2We3345']
lst=[]
for x in items:
	if len(x)<6 or len(x)>12:
		continue
	else:
	    pass
	if not re.search("[a-z]",x):
		continue
	elif not re.search("[A-Z]",x):
		continue
	elif not re.search("[1-9]",x):
	    continue
	elif not re.search("[$@#]",x):
		continue


	else:
		pass
	lst.append(x)
print(lst)'''
'''lst=[('Tuan',20,20),('Lam',18,22),('Trinh',20,22),('Tuan',50,18),('Phuong',9,9)]
print(sorted(lst))'''
'''pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))'''
'''s=input("Nhap mot chuoi: ")
lst=sorted(set(s.split(" ")))
for x in lst:
	print(x,":",s.count(x),sep='')'''
#Thuat toan tim kiem nhi phan
'''lst=[x for x in range(100)]
l=0
r=99
m=int((l+r)/2)
a=56
while(l!=r):
	m=int((l+r)/2)	
	if(lst[m]==a):
		break
	elif(lst[m]>a):
	    r=m	
	elif(lst[m]<a):
		l=m
print(m)'''
#Thuat toan shaker sort
'''lst=[2,8,5,9,4,0,6,1,7,3]
l=0
r=9
mark=9
while(l<r):
	for i in range(r,l,-1):
		if lst[i]<lst[i-1]:
			x=lst[i]
			lst[i]=lst[i-1]
			lst[i-1]=x
			mark=i
	l=mark
	for j in range(l,r):
	    if	lst[j]>lst[j+1]:
	    	y=lst[j]
	    	lst[j]=lst[j+1]
	    	lst[j+1]=y
	    	mark=j
	r=mark
print(lst)	'''








