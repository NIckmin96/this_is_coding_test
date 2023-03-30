# 바닥 공사
n = int(input())
d = [0]*1000
d[1] = 1
d[2] = 3
# 점화식
for i in range(3,n+1) : 
    d[i] = 2*d[i-1] -2*(i-2) + 1
        
print(d[n]%796796)

