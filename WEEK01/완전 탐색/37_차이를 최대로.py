# 10819

n = int(input())
arr = list(map(int, input().split()))

abs_sum_case = []
new_arr = [0] * n
visited = [0] * n


def get_abs_sum(arr):
    abs_sum = 0
    for i in range(n - 1):
        abs_sum += abs(arr[i] - arr[i + 1])
    return abs_sum


def dfs(depth):
    if depth == n:
        abs_sum_case.append(get_abs_sum(new_arr))
        return

    for i in range(n):
        if visited[i] == 1 : continue
        new_arr[depth] = arr[i]
        visited[i] = 1
        dfs(depth + 1)
        visited[i]=0
        new_arr[depth] = 0


dfs(0)
max_value = 0
print(max(abs_sum_case))

