#-*- coding: utf-8 -*-
a=10
b="character"
c=3.14
print(type(a))
print(type(b))
print(type(c))
from decimal import*
getcontext().prec=4
print(Decimal(2)/Decimal(3))
from fractions import*
frac = Fraction(11,132)
frac1 =Fraction(-12,43)
print(frac+frac1)
print(type(frac))
c=complex(2,5)
print(c)
print(type(c.real))
print(type(c.imag))
cc=3**2
print(cc)
char1 ='I\'m a good boy'
char2='''Ai la trieu phu
Mua dong khong lanh
Ai moi la nguoi yeu em
'''
char3="moi"
#len la do dai cua chuoi
char4=char3[len(char3)-1]
'''toqaan tu in tra ve true neu char3 trong char 2 
ve False neu char 3 khong trong char 2''' 

char5=char3 in char2
'''{1:5] lay phan tu [1] den [5-1]
[None:5 tu dau den phan tu [5]]
[None:None],[:] lay ca chuoi'''

char6=char1[1:5]
print(char1)
print(char2)
print(r"Neu mot\n nao do")
print(char4)
print(char6)