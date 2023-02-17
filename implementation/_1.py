# 상하좌우

N = int(input())
A = list(input().split())
# 초기값 지정
x=1
y=1
for direction in A : 
    if direction == 'L' : 
        if y > 1 : 
            y -= 1
    elif direction == 'R' : 
        if y < N : 
            y += 1
    elif direction == 'U' : 
        if x > 1 : 
            x -= 1
    elif direction == 'D' : 
        if x < N : 
            x += 1
            
print(x, y)