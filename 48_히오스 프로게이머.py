# 16564

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
end = start + k

res = 0
while start <= end:
    mid = (start + end) // 2

    hap = 0
    for level in levels:
        if mid > level:
            hap += (mid - level)

    if hap <= k:
        start = mid + 1
        res = max(mid, res)
    else:
        end = mid - 1

print(res)
################################################################################
# ----------dfs로 풀기--------------
# n, k = map(int, input().split())
# champions = []
# for i in range(n):
#     champions.append(int(input()))
# champions.sort()
# levels = [0] * (k + 1)
# for i in range(k + 1):
#     levels[i] = i
#
#
# sum_level = 0
# levelup_champions = champions.copy()
# new_levels=[0]*n
# max_low=0
# def dfs(depth):
#
#     global sum_level, ans, max_low
#     if depth == n:
#         max_low=max(max_low,min(levelup_champions))
#         return
#     for i in range(len(levels)):
#         if sum(new_levels)+levels[i] <= k:
#             new_levels[depth] = levels[i]
#             levelup_champions[depth] += levels[i]
#             dfs(depth + 1)
#             new_levels[depth] = 0
#             levelup_champions[depth] -=levels[i]
# dfs(0)
# print(max_low)
###################################################################