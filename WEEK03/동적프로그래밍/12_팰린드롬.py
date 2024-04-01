# # 10942

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (n)for _ in range(n)]

for i in range(n):
    dp[i][i]=1

for s in range(0,n-1):
    if  arr[s] == arr[s+1]:
        dp[s][s+1] = 1

for s in range( n-2,-1,-1 ):
    for e in range(1,n ):
        if arr[s]==arr[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1


m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
