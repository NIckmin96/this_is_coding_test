# DFS&BFS

## 탐색
- 많은 양의 데이터 중에서 원하는 데이터를  찾는 과정
- 탐색 알고리즘의 대표가 DFS, BFS
- 이를 이해하기 위해서는 기본 자료구조인 **큐, 스택**에 대한 이해가 필요

## 자료구조
- 데이터를 표현, 관리하고 처리하기 위한 구조
- **스택, 큐**는 자료구조의 기초적인 개념
    - **삽입(Push), 삭제(Pop)** 로 구성
    - Overflow : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 Push 연산을 수행할 때 발생
    - Underflow : 특정 자료구조에 데이터가 전혀 없는 상태에서 Pop 연산을 수행할 때 발생
### Stack
- '선입 후출'의 구조(First in Last Out)
- append, pop 사용
### Queue
- '선입 선출'의 구조(First in First Out)
- 줄서기와 비슷
- **deque** 사용
```python
from collections import deque
```
## 재귀함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- Recursive Error
    - 재귀의 최대 깊이를 초과할 때 나오는 에러
- 재귀함수의 수행은 스택 자료구조를 활용
    - 함수를 재귀적으로 호출할때, 가장 마지막에 호출된 함수의 수행이 종료돼야 앞의 함수도 종료할 수 있기 떄문
    > "First in Last out"

## DFS(Depth-First Search)
> "깊이 우선 탐색"
- **그래프**에서 깊은 부분을 우선적으로 탐색하는 알고리즘
    - 그래프의 구성요소
        - Node(노드)
        - Edge(간선)
        - Vertex(정점)
    - 인접 노드(Adjacent Node)
        - 두개의 노드가 간선으로 연결되어 있는 경우
    - 그래프의 표현방식
        1. Adjacency Matrix
            - 2차원 배열에 각 노드가 연결된 형태를 기록
        ```python
        # 연결되지 않은 노드 끼리는 INF
        # 나머지는 Edge의 값(거리)
        INF=9999999999
        graph=[
            [0,7,5],
            [7,0,INF],
            [5,INF,0]
        ]
        print(graph)
        ```
        2. Adjacency List
            - 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
            - **연결 리스트**를 사용
            ```python
            graph=[[] for _ in range(3)]

            # 노드0에 연결된 노드 정보(노드, 거리) 저장
            graph[0].append((1,7))
            graph[0].append((2,5))
            # 노드1에 연결된 노드 정보(노드, 거리) 저장
            graph[1].append((0,7))
            # 노드2에 연결된 노드 정보(노드, 거리) 저장
            graph[2].append((0,5))

            print(graph)
            ```
        - 두 방식의 차이점
            - 메모리적 측면
                - Adjacency Matrix < Adjacency List
            - 노드간 연결 여부 정보 확인
                - Adjacency Matrix > Adjacency List
- 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 Pop
    3. 2번의 과정을 더 이상 수행할 수 없을 떄 까지 반복
- 시간 복잡도
    - $O(N)$
- 재귀함수를 활용해 구현하면 간결하게 구현 가능

## BFS(Breadth First Search)
> '너비 우선 탐색'
- 가까운 노드부터 탐색하는 알고리즘
- Queue방식(*First in First out*) 사용하는 것이 정석
- 동작 방식
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
- 시간 복잡도
    - $O(N)$
- 일반적으로 수행시간이 DFS보다 빠름

## 정리
| |DFS|BFS|
|---|---|---|
|동작 원리|스택|큐|
|구현 방법|재귀함수 이용|큐 자료구조 이용|

# 문제
1. 음료수 얼려먹기
    - https://github.com/NIckmin96/this_is_coding_test/blob/main/DFS_BFS/_1.py 
3. 미로 탈출
