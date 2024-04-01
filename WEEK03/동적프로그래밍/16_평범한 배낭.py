# 12865
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
back=[[0,0]]
for i in range(n):
    w,v=map(int,input().split())
    back.append([w,v])

dp=[[0 for i in range(k+1)]for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        weight=back[i][0]
        value=back[i][1]

        if j<weight: # 현재 물건의 무게가 확인할 dp값보다 작을때
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(value+dp[i-1][j-weight],dp[i-1][j])
print(dp[n][k])

