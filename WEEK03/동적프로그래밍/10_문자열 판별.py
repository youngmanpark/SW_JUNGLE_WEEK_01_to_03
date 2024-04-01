# 16500

import sys
input=sys.stdin.readline

S=input()
n=int(input())
ARR=[]
for i in range(n):
    ARR.append(input().strip())

dp=[0]*len(S)
dp[-1]=1
for i in range(len(S),-1,-1):
    for j in ARR:
        if S[i:len(j)+i]==j and dp[i+len(j)]==1 :
            dp[i]=1

print(dp[0])