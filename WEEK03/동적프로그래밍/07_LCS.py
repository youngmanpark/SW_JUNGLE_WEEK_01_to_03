# 9251
import sys
input = sys.stdin.readline
str1 = list(input().strip())
str2 = list(input().strip())
str1.insert(0,"")
str2.insert(0,"")
dp=[["" for j in range(len(str1))] for i in range(len(str2))]

for i in range(1,len(str2)):
    for j in range(1,len(str1)):
        if str1[j]==str2[i]:
            dp[i][j] = dp[i-1][j-1]+str1[j]
        else:
            if len(dp[i][j-1])>len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

result=dp[-1][-1]
print(len(result))
# if result!="":
#     print(result)
