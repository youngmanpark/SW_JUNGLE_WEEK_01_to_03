# 11053
# -----DP------
# 시간 복잡도 O(n**2)
n = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# # -----이진 탐색------
# # 시간 복잡도 O(nlogn)
# # bisect 사용
# import bisect
#
# x = int(input())
# arr = list(map(int, input().split()))
#
# dp = [arr[0]]
#
# for i in range(x):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = bisect.bisect_left(dp, arr[i])
#         dp[idx] = arr[i]
#
# print(len(dp))