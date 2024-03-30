# 2294
import sys

input = sys.stdin.readline
n, money = map(int, input().split())  # 동전 가지수, 금액
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [[float('inf') for _ in range(money + 1)] for _ in range(n + 1)]

dp[0][0] = 0

for c in range(1, n + 1):  # 코인부터
    for m in range(money + 1):  # 머니머니~
        dp[c][m] = dp[c - 1][m]
        if m-coins[c-1]>=0   :
            dp[c][m] = min(dp[c][m - coins[c - 1]] + 1, dp[c][m])
if dp[n][money] == float('inf'):print(-1)
else: print(dp[n][money])

# dp=[float('inf')]*(money+1)
# dp[0]=0
# for i in range(n):
#     for j in range(coins[i],money+1):
#
#         if dp[j-coins[i]]!=float('inf'):
#             dp[j]=min(dp[j-coins[i]]+1,dp[j])
#
#
# if dp[money]==float('inf'):print(-1)
# else:print(dp[money])