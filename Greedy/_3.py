# 숫자 카드 게임

# N: # of rows / M: # of cols
N,M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
values = [min(arr[i]) for i in range(N)]
print(max(values))
    