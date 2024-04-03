# 15881
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
s=deque(list(input()))
cnt=0
while s:
    if s[0]=='p'and s[1]=='P'and s[2]=='A' and s[3]=='p':
        cnt+=1
        for i in range(4):
            s.popleft()
    else:
        s.popleft()

print(cnt)
