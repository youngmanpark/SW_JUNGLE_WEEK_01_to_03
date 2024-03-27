# 7569
import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())  # 가로,세로,높이

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if tomato[nx][ny][nz] == 0:
                    q.append((nx, ny, nz))
                    tomato[nx][ny][nz] = tomato[x][y][z] + 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                q.append((i,j,k))

bfs()

count = 0
flag=False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                flag=True
            count=max(count,tomato[i][j][k])
if flag==False:
    print(count-1)
else:
    print(-1)
