# 효율적인 화폐 구성

n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

d = [0]*10001
for j in range(m+1) :
    for i in arr :  
        if j%i == 0 : 
            if d[j] == 0 : 
                d[j] = j//i
            else : 
                d[j] = min(d[j], j//i)
                
if d[m] != 0 : 
    print(d[m])
else : 
    print(-1)
    
