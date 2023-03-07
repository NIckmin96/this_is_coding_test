# 두 배열의 원소 교체

n,k = map(int, input().split())
array_a = sorted(list(map(int, input().split()))) # 오름차순
array_b = sorted(list(map(int, input().split())), reverse=True) # 내림차순

for i in range(k):
    if array_a[0] < array_b[0] : 
        array_a[0], array_b[0] = array_b[0], array_a[0]
        array_a = sorted(array_a) # 오름차순
        array_b = sorted(array_b, reverse=True) # 내림차순
    else : 
        break
    
print(sum(array_a))