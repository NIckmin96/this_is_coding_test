# 팀 결성

def find(parent, x):
    if parent[x] != x : 
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b

n,m = map(int, input().split())

parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
    
for _ in range(m): 
    x,a,b = map(int, input().split())
    if x == 0:
        union(parent, a, b)
    elif x == 1:
        a = find(parent, a)
        b = find(parent, b)
        if a == b : 
            print("YES")
        else : 
            print("NO")