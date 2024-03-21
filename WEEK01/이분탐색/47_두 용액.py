# 2470

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1
answer = abs(arr[start] + arr[end])

result = [arr[start],arr[end]]

while start < end:
    left = arr[start]
    right = arr[end]
    sum = left + right

    if abs(sum) < answer:
        answer = abs(sum)
        result = [left,right]

        if answer==0:
            break

    if sum<0 :
        start+=1
    else:
        end -= 1

print(*result)