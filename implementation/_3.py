# 왕실의 나이트

loc = input()
y_lst = ['a','b','c','d','e','f','g','h']
new_y = dict(zip(y_lst, range(1, len(y_lst)+1)))
x = int(loc[1]); y = loc[0] # 1~8 / a~h
y = new_y[y]

if ((x==1)&(y==1)) | ((x==1)&(y==8)) | ((x==8)&(y==1)) | ((x==8)&(y==8)) : 
    ways=2
elif ((x==1)|(x==8)) & ((y>1)&(y<8)) : 
    ways=3
elif ((y==1)|(y==8)) & ((x>1)&(x<8)) : 
    ways=3
elif ((x==2)&(y==2)) | ((x==7)&(y==7)) | ((x==2)&(y==7)) | ((x==7)&(y==2)) : 
    ways=4
elif ((x==2)|(x==7)) & ((y>2)&(y<7)) :
    ways=6
elif ((y==2)|(y==7)) & ((x>2)&(x<7)) :
    ways=6
else : 
    ways=8
    
print(ways)