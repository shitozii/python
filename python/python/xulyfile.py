#ham open tra ve file object
file_object=open('file1.txt')#mode='...'/a a+
data=file_object.read()#size truyen vao la vi tri doc den dong thoi di chuyen con tro toi vi tri nay
#de doc file lan thu 2 ta can dong file bang file_object.close() roi mo lai file
data2=file_object.read()#luc nay con tro da tro toi cuoi file nen print data2 ko co ket qua
file_object.close()
file_object=open('file1.txt')
data_3=file_object.readline()
data_4=file_object.readline()
file_object.close()
#print(data_3)
#print(data_4)
file_object=open('file1.txt')
data_7=file_object.read()
file_object.seek(0)
data_8=file_object.read()
#print(data_7)
#print(data_8)
with open('file1.txt') as fobj:
	 data_9=fobj.read()
	 print(data_9)
	 #doc xong dong file luon

#file_object=open('file1.txt',mode='a+')#mode a+ dua con tro ve cuoi file de ghi tiep (append)

#data_5=file_object.readlines()#=data_5=list(file_object),cac constructor cung dua con tro ve cuoi file
#print(data_5)
print(data_6)