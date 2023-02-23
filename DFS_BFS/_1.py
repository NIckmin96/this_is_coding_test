# 음료수 얼려먹기

N,M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]
def dfs(x,y):
    if (x<0) | (x>=N) | (y<0) | (y>=M) : 
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    else : 
        return False
    
result = 0
for n in range(N) : 
    for m in range(M):
        if dfs(n,m)==True : 
            result+=1
            
print(result)