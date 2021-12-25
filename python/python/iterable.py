'''iteration la thuat ngu chung chi viec lay tung phan tu cua mot doi tuong nao do bang 
vong lap hay mot phuong phap nao do '''
'''iterable object la object co phuong thuc __iter__ tra ve mot iterator 
hoac mot object co phuong thuc __getitem__ cho phep ban lay bat cu phan tu nao = indexing
'''
'''-iterator object la doi tuong cho phep ta lay tung gia tri mot cua no .Tuc la ta khong the lay mot gia tri bat ky
nhu list hay string
-iterator khong co kha nang tai su dung tru mot so iterator 
'''
itera=[x for x in range(4)]
print(itera)
itera2=(n for n in range(3))
#Luc nay sum itera=3
print(next(itera2))
print(next(itera2))
print(next(itera2))
print(sum(itera2))#Luc nay sum dua con tro ve cuoi danh sach nen sum0
print(max(1,2,3))
print(sorted([1,2,3,10,5,6],reverse=True))


