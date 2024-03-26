# 3190

import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

n = int(input()) #보드의 크기
board = [[0] * n for _ in range(n)] #보드 세팅
vis = [[False] * n for _ in range(n)] #방문 처리
k = int(input()) #사과의 개수

# 사과의 위치 1로 세팅
for i in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

# 방향 전환 횟수
L = int(input())
snakes = deque()

# L만큼의 방향 전환 정보
for _ in range(L):
    x, c = input().split()
    snakes.append((x, c))

deq.append((0, 0))
vis[0][0] = True
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #->,v,-<,^
dir_idx = 0
cnt = 0

while deq:
    if snakes and cnt == int(snakes[0][0]):
        _, c = snakes.popleft() #계속 빼기(방향 전환하면)
        if c == "D":
            dir_idx = (dir_idx + 1) % 4  # 오른쪽으로 회전
        else:
            dir_idx = (dir_idx - 1) % 4  # 왼쪽으로 회전

    cnt += 1
    cur = deq[-1]  # 뱀 머리 위치
    nx = cur[0] + directions[dir_idx][0] #다음의 뱀머리 위치 x
    ny = cur[1] + directions[dir_idx][1] #다음의 뱀머리 위치 y
    if nx < 0 or ny < 0 or nx >= n or ny >= n or vis[nx][ny]: #벽을 만났거나 내 몸통을 만났거나
        print(cnt)
        break
    if board[nx][ny] == 1: #사과가 있더라면
        board[nx][ny] = 0 #먹고 사과 없애기
    else: #사과가 없는 곳이라면
        st_x, st_y = deq.popleft() # 내가 가는 경로중 젤 먼저 방문한곳 빼기
        vis[st_x][st_y] = False #몸통 안줄었으니 방문 x

    deq.append((nx, ny))
    vis[nx][ny] = True
