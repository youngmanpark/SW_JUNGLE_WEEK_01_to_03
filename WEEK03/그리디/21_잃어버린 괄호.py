# 1541

import sys

input = sys.stdin.readline
m = input().strip().split('-')

tmp = []
for i in m:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    tmp.append(cnt)

result = tmp[0]
for i in tmp[1:]:
    result -= i

print(result)
