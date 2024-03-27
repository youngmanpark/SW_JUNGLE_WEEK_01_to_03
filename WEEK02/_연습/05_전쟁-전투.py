# 1303
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

graph = [list(input()) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS
def dfs(x, y, color):
    cnt=1
    # 현재 지점 방문 처리
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            # 방문한적이 없으면 현재 지점에서 dfs 호출
            if graph[nx][ny] == color:
                cnt += dfs(nx, ny, color)
    return cnt


white = 0
blue = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            white += (dfs(i, j, 'W')) ** 2
        elif graph[i][j] == 'B':
            blue += (dfs(i, j, 'B')) ** 2

print(white, blue)
