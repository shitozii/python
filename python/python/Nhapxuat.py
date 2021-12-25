print(1,2,3)
print('Nao','Minh','cung','di',sep='\n')
print('Tuan',10,[10],(10,10),sep='')
print('line1',end='')
from time import sleep
print('start...',end='',flush=True)
'''Chu y neu them end='',no se khong in ra start luon'''
sleep(2)
print('end')
with open('Tuan.txt','w') as foj:
	print('Nguyen Minh Tuan',file=foj)
hello="Hello.My name is "
name='Tuan'
for c in hello+name :
 print(c,end='',flush='True')
 sleep(0.1)
