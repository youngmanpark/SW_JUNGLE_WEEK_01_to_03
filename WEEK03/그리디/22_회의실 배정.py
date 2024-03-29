# 1931
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x:(x[1],x[0]))

e_point=0
answer=0
for new_s, new_e in arr:
    if e_point<=new_s:
        answer+=1
        e_point=new_e
print(answer)

