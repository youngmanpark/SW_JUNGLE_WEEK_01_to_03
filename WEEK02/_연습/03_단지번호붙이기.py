# 2667
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
house = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    count=1
    house[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == 1:
            count += dfs(nx,ny)
    return count


cnt=[]
for i in range(n):
    for j in range(n):
        if house[i][j]==1:
           cnt.append(dfs(i,j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)

