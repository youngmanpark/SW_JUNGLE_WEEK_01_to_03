# 2798

# n개에서 3개를 중복 없이 뽑아서 리스트에 담기(될수 있는 모든 케이스) 세개의 합이 m을 넘지 않도록
# 리스트에서 m과의 차이가 가장 작은거 뽑기

n, m = map(int, input().split())
arr = list(map(int, input().split()))
path = [0] * n
all_case = []


def dfs(depth, start):
    if depth == 3:
        if m >= sum(path):
            all_case.append(sum(path))

        return

    else:
        for i in range(start, n):
            path[depth] = arr[i]
            dfs(depth + 1, i + 1)
            path[depth] = 0


dfs(0, 0)

max = 0
for i in all_case:
    if abs(m - max) >= abs(m - i):
        max = i
print(max)
