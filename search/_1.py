# 부품 찾기
import sys

n = int(input())
arr = list((map(int,sys.stdin.readline().rstrip().split())))
m = int(input())
arr2 = list(map(int,sys.stdin.readline().rstrip().split()))

for item in arr2 : 
    if item in set(arr) : 
        print("yes", end = ' ')
    else : 
        print("no", end = ' ')