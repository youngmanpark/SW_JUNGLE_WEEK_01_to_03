# 1065

n = int(input())
result = 0

if n<100:
    result= n

else:
    result=99
    if n==1000:
        result-=1
    for k in range(100, n + 1):
        arr = list(str(k))
        for i in range(len(arr)-2):
            if int(arr[i+1]) - int(arr[i])== int(arr[i + 2]) - int(arr[i + 1]):
                result += 1

print(result)
