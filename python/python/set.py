#set khong chua nhieu hon 1 phan tu trung lap
#set co the chua hashable object nhung ban than no khohng phai hash object nen 
#set khong the chua set
set_1={1,1} #du nhieu phan tu 1 nhung set chi luu 1 gia tri
#set khong luu duoc unhashable object  nhu list va set du no co o trong tuple
#khong the tao mot empty set bang cach thong thuong .{} la type dict
#empty set co the tao bang constructor set=set()
set_2={n for n in range (10)}#set comprehension
set_3=set(("Tuan Nguyen Minh"))#loi the constructor la no giup ban tao mot set 
#voi nhieu ky tu bang cach ghi lien mot mach chu khong can phai tac biet tung chu
#set khong quan tam toi thu tu cac phan tu
print(set_2-set_1)#set 1 lon hon set 2 ra set() (set rong)
print(set_1 & set_2)#intersection
print(set_2 | set_3)#union
print(set_2^set_1)#difference chi ton tai trong set truoc ma khong ton tai trong set sau
print((1,2) in{(1,2),2,3})
print(set_1)
print(set_2)
print(set_3)