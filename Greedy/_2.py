# 큰 수의 법칙

N, M, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
assert N == len(arr)
# 큰 순서대로 정렬(오름차순)
arr = sorted(arr)
res = 0
cnt = 0
while cnt < M : 
    cnt_2 = 0
    while cnt_2 < K : 
        res += arr[-1]
        cnt += 1
        cnt_2 += 1
    res += arr[-2]
    cnt += 1
    cnt_2 += 1

############### Another solution ############### 

rep = M//(K+1)
res = (arr[-1]*K + arr[-2])*rep
print(res)