# 1202

import sys
input=sys.stdin.readline

n,k=map(int,input().split())
bosuck=[]
for i in range(n):
    m,v=map(int,input().split())
    bosuck.append([m,v])

bosuck.sort(key=lambda x:(x[1],x[0]))

sack_c=[]
for i in range(k):
    sack_c.append(int(input()))

# ㅈㅈ 5분남아서 포기