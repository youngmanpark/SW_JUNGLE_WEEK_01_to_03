# 9084
import sys

input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())  # 동전 가지수
    coins = list(map(int, input().split()))  # 동전 금액 집합
    print(coins)
    money = int(input())  # 금액

    dp = [[0 for _ in range(money + 1)] for _ in range(n + 1)]

    dp[0][0] = 1

    for c in range(1, len(coins) + 1):  # 코인부터
        for m in range(money + 1):  # 머니머니~
            dp[c][m] = dp[c - 1][m]
            if m - coins[c - 1] >= 0:
                dp[c][m] += dp[c][m - coins[c - 1]]
    print(dp)
    print(dp[n][money])
