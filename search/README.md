# 순차 탐색(Sequential Search)
> 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 이름대로 순차적으로 데이터를 탐색하는 방법
```python
# 순차 탐색 소스코드
def sequential_search(n,target,array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i]==target:
            return i+1 # 현재의 인덱스 위치 반환

print("생성할 원소의 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n,target,array))
```
## 시간 복잡도
`순차 탐색`은 앞에서부터 순차적으로 데이터를 탐색하기 때문에 N개의 데이터가 있을 때, 최악의 경우 시간 복잡도는 $O(N)$이다.

# 이진 탐색(Binary Search)
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
- 위치를 나타내는 변수 3개를 사용(`시작점, 끝점, 중간점`)
    - 여기서 점은 데이터 값이 아닌 **인덱스**
> 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것
- *e.g. 소주 병뚜껑 숫자 맞히기*
## 수행 방식
1. 시작점, 끝점을 확인하고 중간점을 설정
    - 중간점이 실수인 경우에는 소수점을 drop
2. 타겟값과 중간점의 데이터를 비교하고 중간점의 데이터보다 타겟이 작은 경우, 그 뒤의 데이터는 무시
3. 새롭게 구성된 리스트에서 다시 반복
## 시간 복잡도
- $O(logN) = log_2N$
- 이진 탐색은 한번 확인할 때마다 원소의 개수가 절반씩 줄어든다
- `퀵 정렬`과 공통점이 있음
```python
# 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start, end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target : 
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target : 
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else : 
        return binary_search(array, target, mid+1, end)

# 원소의 개수와 target입력 받기
n,target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 결과 출력
result = binary_search(array, target, 0,n-1)
if result == None : 
    print("원소가 존재하지 않습니다.")
else : 
    print(result + 1)
```
```python
# 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    while start<end : 
        mid = (start+end)//2
        # 찾은 경우 중간점 반환
        if array[mid] == target : 
            return mid
        # 중간점 > target
        elif array[mid] > target : 
            end = mid-1
        # 중간점 < target
        else : 
            start = mid + 1

    return None

# 원소의 개수와 target입력 받기
n,target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 결과 출력
result = binary_search(array, target, 0,n-1)
if result == None : 
    print("원소가 존재하지 않습니다.")
else : 
    print(result + 1)
```

# 트리 자료구조
> 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 스스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적을 사용
- 노드와 노드로 구성되어 있음
## 트리 자료구조의 특징
- 트리는 부모 노드와 자식 노드의 관계를 표현됨
- 트리의 최상단 노드 = `루트 노드`
- 트리의 최하단 노드 = `단말 노드`
- 트리에서 일부를 떼어내도 트리 구조이며 이를 `서브 트리`라 함
- 트리는 파일 시스템과 같이 `계층적이고 정렬된 데이터`를 다루기에 적합
## 이진 탐색 트리
> 트리 자료구조 중에서 가장 간단한 형태\
이진 탐색이 동작 할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조
### 이진 탐색 트리의 특징
- 부모 노드보다 `왼쪽` 자식 노드가 `작다`
- 부모 노드보다 `오른쪽` 자식 노드가 `크다`
### 이진 탐색 트리에서의 탐색 과정
1. 루트 노드부터 방문
    - 타겟값이 루트 노드보다 큰 경우
        - 오른쪽 노드만 확인
    - 타겟값이 루트 노드보다 작은 경우
        - 왼쪽 노드만 확인
2. 반복
3. 자식 노드가 더이상 없을때까지 확인 해도 없다면, 타겟값이 없는 것
### 빠르게 입력 받기
- 이진 탐색 문제는 입력 데이터가 많거나 탐색 범위가 넓은 편
- 이때, input()함수를 사용할 경우 동작 속도가 느려짐
- **sys 라이브러리의 readline()함수를 사용**
```python
# 한줄 입력받아 출력하는 소스코드
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)
```
- 입력후 엔터를 치면 줄 바꿈으로 인식되기 때문에 `rstrip`을 꼭 넣어주어야 한다!
# 문제
1. [부품 찾기](https://github.com/NIckmin96/this_is_coding_test/blob/main/search/_1.py)
2. [떡볶이 떡 만들기](https://github.com/NIckmin96/this_is_coding_test/blob/main/search/_2.py)