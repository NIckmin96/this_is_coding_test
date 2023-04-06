# 미래 도시
import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드, 간선의 개수
n,m = map(int, input().split())
edge = [tuple(map(int,input().split())) for _ in range(m)]
x,k = map(int, input().split())

# 플로이드 워셜(1->k / k->x)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0
for a,b in edge : 
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
if (graph[1][k] + graph[k][x]) >= INF : 
    print(-1)
else : 
    print(graph[1][k] + graph[k][x])