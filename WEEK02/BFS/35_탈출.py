# 3055
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

distance = [[float('inf')] * c for _ in range(r)]



def bfs():
    while q:
        x, y, cur = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'X':  # 범위 안이고 돌이 아닌곳 중에서
                if (board[nx][ny] == '.' or board[nx][ny] == 'D') and distance[nx][ny] == float('inf'):
                    # 비어있는 칸이거나 비버굴이면서 방문하지 않은곳
                    if cur == 's':  # 고슴도치이면 다음칸 이동 시 최소값으로 distance 갱신
                        q.append((nx, ny, cur))
                        distance[nx][ny] = min(distance[nx][ny], distance[x][y] + 1)
                    elif cur == '*':  # 물이면 다음칸이 비버굴인지 확인
                        if board[nx][ny] == 'D': continue
                        q.append((nx, ny, cur))
                        board[nx][ny] = '*'



d_x = 0
d_y = 0
# 고슴 도치 위치 큐 삽입
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            q.append((i, j, 's'))
            distance[i][j] = 0

        elif board[i][j] == '*':
            q.appendleft((i, j, '*'))

        elif board[i][j] == 'D':
            d_x, d_y = i, j
bfs()
d = distance[d_x][d_y]
if d == float('inf'):
    print('KAKTUS')
else:
    print(d)
