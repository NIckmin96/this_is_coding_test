# 성적이 낮은 순서로 학생 출력하기

N = int(input())
dict = {}
array = [input().split() for _ in range(N)]
for name, score in sorted(array, key = lambda x:x[1]) : 
    print(name, end = ' ')