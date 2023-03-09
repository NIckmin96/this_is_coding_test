# 떡볶이 떡 만들기
import sys
n,m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
mean = sum(arr)//n

def binary_search(h):
    residuals = list(map(lambda x:x-h if x-h > 0 else 0, arr))
    if sum(residuals) > m : 
        return binary_search(h-1)
    elif sum(residuals) < m : 
        return binary_search(h+1)
    else : 
        return h
    
ans = binary_search(mean)
print(ans)


