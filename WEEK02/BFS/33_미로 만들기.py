# 2665
import heapq
import sys

input=sys.stdin.readline
n=int(input())

board=[]
for i in range(n):
    board.append(list(map(int,input().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

distance=[[0 for _ in range(n)]for _ in range(n)]
visited = [[False] * n for _ in range(n)]
def bfs(x,y):
    q=[]
    heapq.heappush(q,(0,x,y))
    visited[x][y]=True

    while q:
        count,x,y=heapq.heappop(q)
        if x==n-1 and y==n-1:
            return count
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: #범위 밖으로 나가지 않는 경우와 방문 안했던 경우
                if board[nx][ny]==0:#검은방인 경우
                    heapq.heappush(q,(count+1,nx,ny))
                else: # 흰방인 경우
                    heapq.heappush(q,(count,nx,ny))
                visited[nx][ny]=True


print(bfs(0,0))

