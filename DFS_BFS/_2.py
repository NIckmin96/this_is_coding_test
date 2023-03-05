# 미로 탈출
from collections import deque

N,M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    # queue 구현을 위해 Deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # queue가 빌 때 까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if (nx < 0) | (ny < 0) | (nx >=N) | (ny >= M):
                continue
            # 벽인 경우 무시
            if maze[nx][ny] == 0 : 
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1 : 
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
                
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[N-1][M-1]
    
print(bfs(0,0))
        