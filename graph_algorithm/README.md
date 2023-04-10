# 다양한 그래프 알고리즘

||그래프|트리|
|---|---|---|
|방향성|방향 그래프 혹은 무방향 그래프|방향 그래프|
|순환성|순환 및 비순환|비순환|
|루트 노드 존재 여부|루트 노드가 없음|루트 노드가 존재|
|노드간 관계성|부모와 자식 관계 없음|부모와 자식 관계|
|모델의 종류|네트워크 모델|계층 모델|

- 그래프의 구현 방법(노드: $V$ / 간선: $E$)
    1. 인접 행렬(Adjacency Matrix) : 2차원 배열을 사용
        - 간선 정보 저장을 위해 $O(V^2)$ 만큼의 메모리 필요
        - 노드 A에서 B까지의 비용을 구하는 데 걸리는 시간 : $O(1)$
        - $e.g.$ 플로이드 워셜 알고리즘
        - **노드의 개수가 적은 경우 사용하는 것이 유리**
    2. 인접 리스트(Adjacency List) : 리스트를 사용
        - 간선 정보 저장을 위해 $O(E)$ 만큼의 메모리 필요
        - 노드 A에서 B까지의 비용을 구하는 데 걸리는 시간 : $O(V)$
        - $e.g.$ 다익스트라(Dijkstra) 알고리즘
        - **노드의 개수가 많은 경우 사용하는 것이 유리**

## 서로소 집합
- 공통의 원소가 없는 두 집합
- `union,find` 연산을 활용
    - 이떄, 작은 수의 노드가 부모 노드가 되도록 함
1. 노드의 개수(V)크기의 부모 테이블 초기화
    - 모든 원소가 자기 자신을 부모로 가지도록 설정
2. 각 union 연산의 루트 노드를 찾아서 테이블 업데이트 하기
    - union 1,4 : 1의 부모는 1 / 4의 부모는 1
- **루트 노드를 찾기 위해서, 각 원소의 부모 노드를 거슬러 올라가며 찾기**

```python
# 기본적인 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int, input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end='')
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end= '')
for i in range(1,v+1):
    print(parent[i], end=' ')
```
- 위와 같은 방식의 경우, 'find_parent' 함수가 비효율적으로 동작한다.
    - 최악의 경우, find 함수가 모든 노드를 탐색하기 때문

### 경로 압축 기법
- find 함수를 재귀적으로 호출한 뒤에, 부모 테이블 값을 갱신하는 기법
```python
# 경로 압축 기법 소스코드(find)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```
- 위의 방식으로 수정하게 되면, 루트 노드가 바로 부모 노드로 업데이트 됨

```python
# 개선된 서로소 집합 알고리즘 소스코드

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int, input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end='')
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end= '')
for i in range(1,v+1):
    print(parent[i], end=' ')
```

### 서로소 집합 알고리즘의 시간 복잡도
- 노드의 개수가 $V$, 최대 $V-1$개의 Union 연산과 $M$개의 find 연산이 가능할 때, **경로 압축 방식**을 적용한 시간 복잡도는 $O(V+M(1 + log_{2-M/V}{V}))$

## 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있음
    - 방향 그래프 : DFS를 사용

0. 모든 노드에 대해 자기 자신을 부모로 설정하는 부모 테이블 초기화
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    - 루트 노드가 서로 다르다면, 두 노드에 대하여 union 연산 수행
    - 루트 노드가 같다면, 사이클이 발생
2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복

- 간선의 개수가 E일 때, 모든 간선을 하나씩 확인
- 매 간선에 대하여 union, find 함수를 호출

```python
# 서로소 집합을 활용한 사이클 판별 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v,e = map(int, input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생한 후 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 union 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```

## 신장 트리
> 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

### 크루스칼 알고리즘
- **최소 신장 트리 알고리즘**의 대표적인 유형
    - *e.g. N개의 도시가 있을 떄, 두 도시에 도로를 놓아 전체 도시가 연결될 수 있도록 도로를 설치하는데 드는 최소 비용을 구하는 문제*
- **그리디** 알고리즘으로 분류
- 알고리즘 수행방법
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
        - 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함
        - 사이클이 발생하는 경우, 포함 X
    3. 모든 간선에 대하여 2번의 과정 반복
> 가장 거리가 짧은 간선부터 차례대로 집합에 추가하기
```python
# 크루스칼 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b

v,e = map(int, input().split())
parent = [0]*(v+1)

edges = [] # 간선을 담을 리스트
result = 0 # 최종 비용을 담을 변수

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```
- 시간 복잡도
    - 간선의 개수가 $E$일때, $O(ElogE)$

## 위상 정렬
- *정렬 알고리즘*의 일종
> 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 정렬하는 것'
- *e.g. '선수과목을 고려한 학습 순서 설정'*
- `진입 차수`
    - 특정 노드로 '들어오는' 간선의 개수
- 알고리즘 수행방식
    1. 진입 차수가 0인 노드를 큐에 넣는다
    2. 큐가 빌때까지 다음의 과정을 반복한다.
        1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
        2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
    - *모든 원소를 방문하기 전에 큐가 빈다면, 사이클이 존재*
- 위상 정렬의 답안
    - 여러가지가 존재할 수 있음
    - 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우

```python
# 위상 정렬 소스코드
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v,e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동가능
    # 진입 차수를 1증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지 반복
    while q : 
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 수행 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
```
- 위상 정렬의 시간 복잡도
    - $O(V+E)$

## 문제
1. [팀 결성]()
2. [도시 분할 계획]()
3. [커리큘럼]()