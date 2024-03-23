# 13334

import sys
import heapq
input = sys.stdin.readline

n = int(input())
office = []

# n명의 사람들의 사무실과 집위치를 (가까운곳-먼곳)순으로 큐에 담아준다
for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    heapq.heappush(office, (end, start))





d = int(input())

possible = []
res = 0
cnt = 0
while office:
    end, start = heapq.heappop(office)
    if start >= end - d:
        heapq.heappush(possible, (start, end))
        cnt += 1
    while possible:
        s, e = heapq.heappop(possible)
        if s < end - d:
            cnt -= 1
        else:
            heapq.heappush(possible, (s, e))
            break
    res = max(res, cnt)
print(res)