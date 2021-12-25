'''class Map_Class:
	def keys(self):
	  return[1,2,3]
	  def __getitem__(self,key):
	    return key * 2'''
#Mot object la mapping object neu no co du ca 2 phuong thuc keys va __getitem___
dic={'Tuan':'Dep trai','DC':100}#phan tu trong list phai la hash object
dic_1={}#empty dict
#dict comprehension
dic_2={key:value for key, value in [('Tuan',"Dep trai"),('DC',100)]}
#Constructor
#dict rong
dic_3=dict()
#iterable
iter_=[('Tuan','DC'),('Dep trai',100)]
dic_4=dict(iter_)
#keyword arguements
dic_5=dict(x="Dep trai",y=100)
#fromkeys:
iter_1=('Tuan','DC')
dic_6=dict.fromkeys(iter_1,69) #khoi tao gia tri none neu khong khai bao gi sau iter_1
print(dic_6)
print(type(dic_6))
#dict la unhashable object nen ta co the thay doi truc tiep gia tri
dic['Tuan']='On-slaught'#neu ta gan mot key word chua ton tai trong dict thi dict se tu them no vao
print(dic)
#---------------------------------------
#Phuong thuc
print(dic.copy())
dic.clear()
print(dic)
print(dic_2.get('Tuan'))#con co the khai bao 1 cai dang sau de neu keyy khong co o trong co the tra ve gia  tri nay
print(list(dic_2.items()))#tra ve tuple
print(list(dic_2.keys()))
print(list(dic_2.values()))
print(dic_2.pop('Tuan'))#tuy nhien se dong thoi xoa luon key 'Tuan'va gia tri cua key 'Tuan' trong dict luon
print(dic_2.setdefault('DC'))#neu dua vao mot key chua do thi se tu them key do vao trong dict voi gia tri default(neu chua khai bao)
#cap nhat dict (bai kiem tra)
d={'a':1} 
E=[('b',2),('c',3)]#d goi la packing argument
d.update(E)
print(d)
d.update(b=10)
print(d)
