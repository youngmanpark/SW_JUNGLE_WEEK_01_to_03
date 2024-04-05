# 1202

import sys
import heapq
input=sys.stdin.readline

n,k=map(int,input().split())
bosuck=[]
for i in range(n):
    heapq.heappush(bosuck,list(map(int,input().split())))

bags=[]
for i in range(k):
    bags.append(int(input()))
bags.sort()

answer=0
tmp=[]
for bag in bags:
    while bosuck and bag>=bosuck[0][0]:
        heapq.heappush(tmp,-heapq.heappop(bosuck)[1])
    if tmp:
        answer-=heapq.heappop(tmp)
    elif not bosuck:
        break
print(answer)
