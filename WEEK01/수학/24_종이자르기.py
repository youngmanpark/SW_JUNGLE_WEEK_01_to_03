# 2628
x, y = map(int, input().split())
arr_x = [0]
arr_y = [0]
arr_x.append(x), arr_y.append(y)
n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    if (a == 1):
        arr_x.append(b)
    else:
        arr_y.append(b)
arr_x.sort()
arr_y.sort()
max_x = 0
max_y = 0
for i in range(len(arr_x) - 1):
    if max_x < arr_x[i + 1] - arr_x[i]:
        max_x = arr_x[i + 1] - arr_x[i]
for i in range(len(arr_y) - 1):
    if max_y < arr_y[i + 1] - arr_y[i]:
        max_y = arr_y[i + 1] - arr_y[i]
print(max_x*max_y)
