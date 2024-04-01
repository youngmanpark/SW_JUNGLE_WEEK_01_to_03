# 10942

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [[0] * (n + 2)for _ in range(n+2)]

for i in range(n):
    dp[i][i]=1

for s in range(n-1):
    if  arr[s] == arr[s+1]:
        dp[s][s+1] = 1

for s in range(1, n + 1):
    for e in range(1, n + 1):
        if s <= e:
            if arr[s]==arr[e] and dp[s + 1][e - 1] == 1:
                dp[s][e] = 1

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])



# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# # dp[i][j] will store whether substring from index i to j is a palindrome or not
# dp = [[0] * (n + 1) for _ in range(n + 1)]
#
# # Initialize palindrome of length 1
# for i in range(n):
#     dp[i][i] = 1
#
# # Initialize palindrome of length 2
# for i in range(n - 1):
#     if arr[i] == arr[i + 1]:
#         dp[i][i + 1] = 1
#
# # Fill dp array for palindromes of length >= 3
# for length in range(3, n + 1):
#     for i in range(n - length + 1):
#         j = i + length - 1
#         if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:
#             dp[i][j] = 1
#
# m = int(input())
# for _ in range(m):
#     s, e = map(int, input().split())
#     print(dp[s - 1][e - 1])