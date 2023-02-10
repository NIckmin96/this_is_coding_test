# 거스름돈

N = int(input())
cnt = 0
for i in [500, 100, 50, 10] : 
    cnt += N//i
    N = N%i
