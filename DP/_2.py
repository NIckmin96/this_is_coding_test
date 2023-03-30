# 개미 전사

import sys

n = int(input())
arr = list(map(int, input().split()))
d = [0]*n

# DP(Bottom-up)
d[0] = arr[0]
d[1] = arr[1]
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+arr[i])
    
print(d[n-1])