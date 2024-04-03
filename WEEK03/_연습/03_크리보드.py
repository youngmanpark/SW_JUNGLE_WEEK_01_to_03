#11058
num =int(input())
data=[i for i in range(num+1)]

for i in range(7,num+1):
    data[i]=max(data[i-3]*2, data[i-4]*3, data[i-5]*4)

print(data[num])

###########################################################
n = int(input())

dp = [0] * (n + 1)

if n <= 6:
    print(n)
    exit(0)

for i in range(1, 7):
    dp[i] = i

for i in range(7, n + 1):
    for j in range(3, n + 1):
        if i - j < 0:
            break
        dp[i] = max((j - 1) * dp[i - j], dp[i])

print(dp[n])