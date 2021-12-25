a=1
print(a)
lst=[1,2,3]
lst_=[1,2,3]
print(lst==lst_)
print(lst is lst_)
print(1>2 or 1<2 )
print(3>2 and 4<2 )
print(not False)
print(True+1)
#gia tri cua true la 1 gia tri cua False la 0
#bool cua chuoi,list,set,tuple,dicit rong,so 0,None deu la false
#chu y cac so tu -5 den 256 hoac la kieu chuoi duoi 20 ky tu
#thi cac bien co cung gia tri se co cung gia tri tra ve tu ham id
#k=4 k=5 k=6 thay bang k in [4,5,6]
#-------------------------------------------
a=1
if a<0:
	print('a nho hon khong')
else :
	print('a lon hon khong')

a=1
b=4
c=3
max=a
if a<b:
	max=b
if max<c:
	max=c
print(max)
#try va except
print(tuple(range(6,3,-2)))#co ho tro indexing(chay tu start den stop-step)
a=4
print(a in range(0,5))
St_list=['Long','Hai','Nguyen']
gen=list(enumerate(St_list,1))
for x,y in gen:
	print(str(x)+'.'+str(y))
