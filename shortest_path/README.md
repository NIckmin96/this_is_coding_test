# 최단 경로
> '길 찾기' 문제
- 보통 **그래프**를 이용해 표현

- 대표적인 최단 경로 알고리즘
    - `다익스트라, 플로이드 워셜, 벨만 포드` 알고리즘

- **Greedy, DP** 알고리즘이 최단 경로 알고리즘에도 적용됨

## 다익스트라(Dijkstra)
> 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

- '음의 간선'이 없을 때 정상적으로 동작

- GPS 소프트웨어의 기본 알고리즘으로 채택

- **Greedy** 알고리즘으로 분류 됨

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
    - 무한에 가까운 수로 초기화($e^9$)
3. 방문하지 않는 노드 중, 최단 거리가 가장 짧은 노드 선택
    - *Greedy 알고리즘의 특성*
4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 업데이트
5. 3번과 4번 반복

### 1. 간단한 다익스트라 알고리즘
- 시간 복잡도 : $O(V^2)$
    - $V$ : 노드의 개수
1. 각 노드에 대한 최단 거리를 담는 1차원 리스트 선언
2. **단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인**
```python
# 간단한 다익스트라 알고리즘 소스코드
import sys
# input함수를 sys.stdin.readline으로 치환
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드의 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 리스트 생성
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if (distance[i] < min_value) and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결괸 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 거리를 출력
    else : 
        print(distance[i])
```
- 간단한 다익스트라 알고리즘의 시간 복잡도
    - $O(V^2)$
    - V번에 걸쳐 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야하고 현재 노드와 연결된 노드를 일일이 확인하기 때문

### 개선된 다익스트라 알고리즘
- Heap(힙) 자료구조 사용
- 자료 구조

|자료구조|추출되는 데이터|
|---|---|
|스택(stack)|가장 나중에 삽입된 데이터|
|큐(Queue)|가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)|가장 우선순위가 높은 데이터|

> Heap \
    - 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나
    - 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제 \
    - 라이브러리 : `PriorityQueue` or `heapq` \
    - 물건 데이터를 (가치, 물건)으로 묶어서 자료구조에 삽입 \
    - 항상 '가치'가 높은 데이터가 먼저 나오게 됨 \
    - 최소 힙(Min heap): 값이 낮은 데이터가 먼저 삭제 \
    - 최대 힙(Max heap): 값이 큰 데이터가 먼저 삭제 
- 하나의 데이터에 대한 시간 복잡도

|우선순위 큐 구현 방식|삽입 시간|삭제 시간|
|---|---|---|
|리스트|$O(1)$|$O(N)$|
|힙(heap)|$O(logN)$|$O(logN)$|

- **알고리즘 자체는 동일하지만, 사용하는 자료구조가 다를 뿐!**
    - 현재 가장 가까운 노드를 앞쪽에 저장하기 위한 목적으로만 우선순위 큐를 추가적으로 이용하는 것

- 

- 개선된 다익스트라 알고리즘의 시간 복잡도
    - 최악의 경우에도 $O(ElogV)$를 보장
    - $V$: 노드의 개수 / $E$ : 간선의 개수

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드의 연결되어 있는 노드에 대한 정보를 담는 리스트 선언
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b노드로 가는 비용 = c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist : 
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# dijkstra 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF : 
        print("INFINITY")
    else :
        print(distance[i])
```
## 플로이드 워셜 알고리즘
> 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 경우 사용
- 짧은 소스 코드
- 단계마다 거쳐 가는 노드를 기준으로 알고리즘 수행
    - 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 X
- 노드의 수가 N일 떄, N번의 단계 수행
    - 단계마다 $O(N^2)$
    - 총 $O(N^3)$
- 2차원 리스트에 *최단 거리* 정보 저장
    - 다익스트라 : 1차원 리스트(출발 노드 1개이기 떄문)
- Dynamic Programming 알고리즘 기반
    - 다익스트라 : Greedy 알고리즘 기반
- 현재 확인하고 있는 노드를 제외하고, N-1개의 노드 중에서 서로 다른 노드쌍을 선택하고 각 조합의 비용을 확인한 뒤, 최단 거리 갱신
    - $O(_{N-1}P_2) = O(N^2)$
- 점화식
    - $D_{ab} = min(D_{ab}, D_{ak}+D_{kb})$
    - $A \rightarrow B$의 최소 비용과 $A \rightarrow K \rightarrow B$의 최소 비용 비교
```python
# 플로이드 워셜 알고리즘 소스코드
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1) : 
    for b in range(1,n+1):
        if a==b : 
            grpah[a][b] = 0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, INFINITY
        if graph[a][b] == INF:
            print("INFINITY")
        else : 
            print(graph[a][b], end=' ')

    print()
```