#1978
n=int(input())
arr=list(input().split(" "))
result=n
for k in arr:
    if int(k)==1:
        result-=1
    for i in range(2,int(k)):
        if int(k)% i==0:
            result-=1
            break
print(result)