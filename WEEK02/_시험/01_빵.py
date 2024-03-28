# 25377
import sys
input=sys.stdin.readline
n=int(input())
min_count=1001

for i in range(n):
    a,b=map(int,input().split())
    if a<=b:min_count=min(min_count,b)

if min_count==1001:
    print(-1)
else:
    print(min_count)

