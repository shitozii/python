#default phai dat o cuoi parameter
def hocdi(kteam=[]):
	kteam.append(10)
	print(kteam)
#neu khai bao ca positional va keyword thi keyword phai o phia sau
#dau sao khai bao o sau tat ca deu la keyword argument,key-word only neu khong co default value
#neu truyen duoi dang positional se bao loi
#co the dat dau * truoc tuple hay list(unpacking) de truyen tuan tu mot lst vao trong
#tuy nhien no o dang positional nen hay can than voi only-keyword argumen
def tuan(*arg):#(pack)#chu y neu co khai bao them mot bien thi khi khai bao ham o phia duoi phai dung keyword
	print(arg)
tuan(*('Tuan','Dep','Trai'))#unpack	
def ngudi(name,ID):
	print(name)
	print(ID)
dic={'name':'Tuan','ID':'20194876'}	
ngudi(**dic)#unpack lan 1 ra key ,unpack lan 2 ra value tuy nhien bien o phan def phai la ten cua key
#locals() globals()
tinh= lambda a,b,c=3:(a+b+c)#lambda la 1 expression
print(tinh(1,2))
find_greater=lambda x,y:x if x>y else y
print(find_greater(2,3))
#map la mo dang generator lay tung phan tu iterable roi goi ham fuc
def inc(x): return x+1
kteam=[1,2,3,4]
print(list(map(inc,kteam)))#lay tung gia tri
#ca filter ca maq deu tra ve generrator expression


