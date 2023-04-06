# 전보
import sys
input = sys.stdin.readline
# node, edge, target
n,m,c = map(int, input().split())

# make graph
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

# start, end, cost
for _ in range(m) : 
    x,y,z = map(int, input().split())
    graph[x][y] = z

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
cnt = 0
cost = []
for i in graph[c]:
    if (i == INF) | (i==0):
        continue
    else : 
       cnt+=1
       cost.append(i)
print(cnt, max(cost))