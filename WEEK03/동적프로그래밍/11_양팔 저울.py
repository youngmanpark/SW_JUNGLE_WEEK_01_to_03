# 2629

import sys

input = sys.stdin.readline
n = int(input())  # 추의 개수
weights = list(map(int, input().split()))
k = int(input())
balls = list(map(int, input().split()))

tmp = [0]
dp = [0] * 40001

for weight in weights:
    for i in range(len(tmp)):
        tmp.append(abs(tmp[i]-weight))
        tmp.append(tmp[i]+weight)
    tmp=set(tmp)
    tmp=list(tmp)

for i in tmp:
    dp[i]=1

for i in balls:
    if dp[i]==1: print("Y",end=" ")
    else: print("N",end=" ")