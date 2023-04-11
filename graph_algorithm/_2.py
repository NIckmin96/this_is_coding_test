# 도시 분할 계획
## 최소 신장 트리

n,m = map(int, input().split())
edges = []
parent = [0]*(n+1)
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b
        
for edge in edges : 
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
         union(parent, a, b)
         result += cost
         last = cost
         
print(result - last)