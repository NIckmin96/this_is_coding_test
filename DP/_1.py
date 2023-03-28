# 1로 만들기
x = int(input())

# 1. 1 빼기를 할 경우
arr = list(range(x))
# 2. 나누기를 할 경우
arr2 = arr.copy()

def func(x):
    if x%5 == 0:
        return x//5
    elif x%3 == 0:
        return x//3
    elif x%2 == 0:
        return x//2
    else : 
        return x
    
arr2 = list(map(func, arr2))

cnt = 0
while x > 1 : 
    if arr[x-1] > arr2[x-2] : 
        x = arr2[x-1]
    elif arr[x-1] < arr[x-1] : 
        x = arr[x-1]
    else : 
        x = arr[x-1]
    cnt +=1
    
print(cnt)