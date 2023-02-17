# 게임 개발
# 방문한 칸의 수 출력 / 바다:1, 육지:0, 가본 곳:-1 / 방향 : 0,1,2,3(북,동,남,서)
# 풀이 방법
'''
- 문제에 설명된 기능중, 필요한 기능을 함수로 정리해서 사용 
-> 이 편이 개인적으로 깔끎하고 알고리즘을 직관적으로 파악하기도 쉽기 때문에

- 기능 구현 후, 문제의 로직에 맞게 main code 구현
'''
##################### 풀이 #####################
# input
N,M = list(map(int, input().split()))
assert (N >= 3) & (M <= 50)
A,B,d = list(map(int, input().split()))
map = [list(map(int, input().split())) for _ in range(N)]

def check_forward() : 
    if d==0 : 
        if map[A-1][B]==0 : 
            return True
        else : 
            return False
    elif d==1 : 
        if map[A][B+1]==0 : 
            return True
        else : 
            return False
    elif d==2 : 
        if map[A+1][B]==0 : 
            return True
        else : 
            return False
    elif d==3 : 
        if map[A][B-1]==0 : 
            return True
        else : 
            return False
        
def move(A,B,d):
    if d==0 : 
        A-=1
    elif d==1 : 
        B+=1
    elif d==2 : 
        A+=1
    elif d==3 : 
        B-=1 
    map[A][B] = -1
    visit.append((A,B))
    return A,B
            
def check_behind() :
    if d==0:
        if map[A+1][B] == 1 : 
            return False
        else : return True
    elif d==1:
        if map[A][B-1] == 1 : 
            return False
        else : return True
    if d==2:
        if map[A-1][B] == 1 : 
            return False
        else : return True
    if d==3:
        if map[A][B+1] == 1 : 
            return False
        else : return True

def backward(A,B,d) : 
    if d==0 : 
        A+=1
    elif d==1:
        B-=1
    elif d==2:
        A-=1
    elif d==3:
        B+=1
    visit.append((A,B))
    return A,B

visit = [(A,B)]
map[A][B]=-1
breakpoint=False
patience=0
d-=1
if d==-1 : 
    d=3
while True :
    if check_forward() : 
        A,B = move(A,B,d)
        patience=0
    else : 
        d-=1
        patience+=1
        if d==-1 : 
            d=3
        
    if patience==4 : 
        if check_behind():
            A,B = backward(A,B,d)
            break
        else : 
            breakpoint=True
            break

print(len(set(visit)))

