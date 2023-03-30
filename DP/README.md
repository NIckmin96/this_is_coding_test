# DP(Dynamic Programming)
> 중복되는 연산을 줄이자

- 컴퓨터는 연산 속도에 한계가 있고, 메모리 용량의 한계도 있기 때문에 **효율적인 알고리즘**을 작성해야 한다.
- 하지만, 어떤 경우는 메모리 공간을 조금 더 사용하면 연산속도를 비약적으로 증가시킬 수 있다.
    - 대표적인 방법이 `Dynamic Programming(DP; 동적 계획법)`

## 점화식
- 인접한 항들 사이의 관계식을 통해서 수열의 항이 이어지는 형태를 **간결하게** 표현하는 방법
    - 피보나치 수열 : $a_{n+2}=f(a_{n+1},a_n)=a_{n+1}+a_n$
- 점화식을 코드로 작성하려면 **재귀 함수**를 사용하면 간단하다.
```python
# 피보나치 함수 소스코드
def fibo(x):
    if (x==1) or (x==2) : 
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
```
- **재귀 함수로만 구현하게 되면 똑같은 연산을 여러번 수행하기 때문에 비효율적**

## DP 사용의 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

### 메모이제이션(Memoization)
- DP를 구현하는 방법중 하나
- 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져와서 사용
    - 똑같은 값을 다시 연산할 필요가 없음

```python
# 피보나치 수열 소스코드(재귀적)

# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0]*100

# 피보나치 함수를 재귀함수로 구현(Top-Down DP)
def fibo(x):
    # 종료 조건
    if (x==1) or(x==2):
        return 1
    # 이미 계산한 적 있다면 그대로 반환
    if d[x] != 0 : 
        return d[x]
    # 아직 계산한 적 없다면 점화식에 따라서 피보나치 연산
    d[x] = fibo(x-2)+fibo(x-1)

    return d[x]

print(fibo(99))
```
### DP를 사용했을 떄, 피보나치의 시간 복잡도
- $O(N)$


### Top-Down / Bottom-Up
- `Top-Down`
    - 큰 문제를 해결하기 위해 작은 문제를 호출 하는 방식
        - 재귀 함수 이용
        - **Memoization**
```python
# 호출되는 함수 확인
d = [0]*100

def pibo(x):
    print('f('+str(x)+')', end=' ')
    if (x==1) or (x==2):
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1)+pibo(x-2)

    return d[x]

pibo(6)

# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)
```
- `Bottom-Up`
    - 작은 문제부터 차근차근 답을 도출
        - 단순 반복문 활용
```python
# 피보나치 수열 소스코드(반복적, Bottom-up)
d = [0]*100
# 첫번째, 두번째 피보나치는 1
d[1], d[2] = 1,1
n = 99

# 피보나치 함수를 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])
```
> Tip : `sys.setrecursionlimit()` 함수를 사용하면 재귀 제한을 완화할 수 있다.

## 문제
1. [1로 만들기](https://github.com/NIckmin96/this_is_coding_test/blob/main/DP/_1.py)
    - [Solution](https://github.com/NIckmin96/this_is_coding_test/blob/main/DP/_1_sol.py)
2. [개미 전사](https://github.com/NIckmin96/this_is_coding_test/blob/main/DP/_2.py)
3. [바닥 공사](https://github.com/NIckmin96/this_is_coding_test/blob/main/DP/_3.py)
4. [효율적인 화폐 구성](https://github.com/NIckmin96/this_is_coding_test/blob/main/DP/_4.py)