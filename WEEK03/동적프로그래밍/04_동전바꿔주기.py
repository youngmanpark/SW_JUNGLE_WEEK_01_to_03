# 2624
import sys

input = sys.stdin.readline

t = int(input())  # 금액
k = int(input())  # 동전 가지수
coins = [[0, 0]]
for _ in range(k):
    a, b = map(int, input().split())
    coins.append([a, b])
dp = [[0 for _ in range(t + 1)] for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):  # 코인 부터
    val, cnt = coins[i]
    for j in range(t + 1):
        dp[i][j] = dp[i - 1][j]
        for c in range(1, cnt + 1):
            if j - c * val >= 0:  # 현재 금액-(동전 개수 * 동전의 가치) 0이상
                dp[i][j] += dp[i - 1][j - c * val]
            else:
                break

print(dp[k][t])
