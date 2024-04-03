# 14916

import sys
input=sys.stdin.readline
n=int(input())
coins=[2,5]
dp=[float('inf') for _ in range(n+1)]
dp[0]=0

for m in range(n+1):
    for coin in coins:
     if m-coin>=0:
         dp[m]=min(dp[m-coin]+1,dp[m])

if dp[n]==float('inf'):print(-1)
else:print(dp[n])