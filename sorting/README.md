# 정렬(Sorting)
> 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
- 정렬 알고리즘으로 데이터를 정렬하면 *이진 탐색*이 가능해짐
- 정렬 알고리즘은 *이진 탐색*의 __전처리 과정__

## 선택 정렬(selection sorting)
> 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정의 반복
- N개의 데이터가 있는 경우, 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료된다. 
```python
# 선택 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
```
- python에서는 위와 같이 리스트 내 두 원소의 위치를 변경할 수 있지만, 다른 프로그래밍 언어에서는 명시적으로 **임시 변수**를 만들어 두 원소의 값을 변경
```python
# python swap 소스코드
array = [3,5]
array[0], array[1] = array[1], array[0]

print(array)
```

```C
// C언어로 구현한 스와프 예제
int a = 3;
int b = 5;

//swap
int temp = a; // 임시 저장 변수 선언
a = b;
b = temp;
```
### 선택 정렬의 시간 복잡도
- $N+(N-1)+(N-2)+...+2$
- 위를 근사치로 표현하면, $N*(N+1)/2 == (N^2+N)/2$
- 간단히 $O(N^2)$로 나타낼 수 있음
    - `선택 정렬`은 기본 정렬 라이브러리를 포함, 다른 정렬 알고리즘과 비교했을 때, 매우 비효율적임
---
## 삽입 정렬(Insertion Sort)
> '데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?'
- `삽입 정렬`은 필요할 때만 위치를 바꾸기 때문에 **'데이터가 거의 정렬 되어 있을 때'** 더욱 효율적이다.
- `삽입 정렬`은 특정 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지는 이미 정렬되어 있다고 가정함
- `삽입 정렬`에서는 특정 데이터가 삽입될 위치를 선택할 때, 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면 됨
```python
# 삽입 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)): 
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]:  한칸씩 앞으로 이동#
            array[j], array[j-1] = array[j-1], array[j]
        else : # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```
### 삽입 정렬의 시간 복잡도
- $O(N^2)$
- 이중 for문을 사용하기 때문에 선택 정렬과 기본적으로는 같은 시간 복잡도를 가지고 있음
- 하지만, 이미 정렬된 데이터가 많은 경우에는 효율적
- `정렬이 거의 되어 있는 상황`에서는 *퀵 정렬* 보다 강력함
---
## 퀵 정렬
- 정렬 알고리즘 중, 가장 많이 사용되는 알고리즘
    - cf) *병함 정렬* 알고리즘
> '기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?'
- `퀵 정렬`은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
- **Pivot**
    - 큰 숫자와 작은 숫자를 교환할 때의 '기준'
    - 피벗을 설정하고 리스트를 분할하는 방법도 여러가지가 존재
        - 대표적인 방법 : **호어 분할**
- 호어 분할(Hoare Partition)
    1. 리스트에서 **첫번째** 데이터를 피벗으로 설정
    2. 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
    3. 큰 데이터와 작은 데이터의 위치를 서로 교환
    4. 반복
        - **이 과정에서 작은 데이터와 큰 데이터의 위치가 엇갈리는 경우, 작은 데이터와 피벗의 위치를 교환**
    - 이 과정을 거치면 피벗 왼쪽의 데이터는 피벗보다 작고, 오른쪽의 데이터는 피벗보다 큰 데이터
        - 이 작업을 분할(Divide), 파티션(Partition)이라고 함
    - 이 상태에서 왼쪽과 오른쪽을 개별적으로 정렬
        - 다시 피벗 설정 후, 위의 과정 반복
        - *재귀 함수*와 동작 원리가 같음
        - 종료 조건 : 재귀 함수가 선언된 리스트의 개수가 1개인 경우
```python
# 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소의 개수가 1개인 경우 종료
        return
    pivot = start # pivot은 첫번째 원소
    left = start + 1
    right = end
    while left <= right: 
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while (left <= end) and (array[left] <= array[pivot]) : 
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while (right > start) and (array[right] >= array[pivot]) : 
            right -= 1
        if left > right : # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```
```python
# 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot  = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
- `퀵 정렬`의 시간 복잡도
    - 평균 시간 복잡도 : $O(NlogN)$
    - 리스트의 가장 왼쪽 데이터를 피벗으로 삼고, **이미 데이터가 정렬되어 있는 경우**에는 퀵 정렬이 매우 느리다.
        - 이 경우, **삽입 정렬**이 효과적
---
## 계수 정렬(Count Sort)
> 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때**만 사용 가능
- **가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크지 않을 때** 사용 가능 
    - *e.g. "0 이상 100 이하인 성적 데이터를 정렬할 때"*
    - **`계수 정렬`을 이용할 때에는 `모든 범위`를 담을 수 있는 크기의 `리스트`를 선언해야 하기 때문**
- `계수 정렬`은 비교 기반의 정렬 알고리즘이 아님
- `계수 정렬`의 작동 방식
    1. 가장 작은 데이터 ~ 큰 데이터 까지의 범위가 모두 담길 수 있도록 하나의 리스트를 생성
        - 처음에는 리스트의 모든 값이 0이 되도록 초기화
    2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 (새로 생성된 리스트)인덱스의 데이터를 1씩 증가
    3. 0부터 끝까지 데이터의 값대로 인덱스를 출력
```python
# 계수 정렬 소스코드

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
### 계수 정렬의 시간 복잡도
- 데이터의 개수가 N이고 최대값의 크기를 K라고 할 때,
    - $O(N+K)$
- 데이터의 범위만 한정되어 있다면 효과적이며, 사실상 현존하는 정렬 알고리즘 중 `기수 정렬(Radix Sort)`과 더불어 가장 빠르다고 볼 수 있음
---
## 파이썬의 정렬 라이브러리
- `sorted()`
    - 퀵 정렬과 비슷한 병합 정렬을 기반으로 함
    - 최악의 경우에도 $O(NlogN)$을 보장함
    - 리스트, 집합이나 딕셔너리 자료형 등을 입력받아 리스트 자료형의 정렬된 결과값을 반환함
```python
# sorted 소스코드
array = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)
```
- `sort()`
    - 리스트 객체의 내장 함수
    - 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬됨
```python
# sort 소스코드
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)
```
- `key`
    - sorted나 sort를 사용할 때, key를 매개변수로 받을 수 있음
    - 하나의 함수가 key로 들어가야함
    - 들어가는 함수가 **정렬의 기준**
```python
# key를 활용한 정렬 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
```
### 정렬 라이브러리의 시간 복잡도
- 정렬 라이브러리는 최악의 경우에도 $O(NlogN)$을 보장

# 문제
1. [위에서 아래로](https://github.com/NIckmin96/this_is_coding_test/blob/main/sorting/_1.py)
2. [성적이 낮은 순서로 학생 출력하기](https://github.com/NIckmin96/this_is_coding_test/blob/main/sorting/_2.py)
3. [두 배열의 원소 교체](https://github.com/NIckmin96/this_is_coding_test/blob/main/sorting/_3.py)