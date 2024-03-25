# 18352
import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)


def bfs(start):
    queue = deque([start])
    distance[start] = 0
    while queue:
        now = queue.popleft()
        # 현재 도시에서 이동할 수 있는 모든 도시를 확인

        for next in graph[now]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[now] + 1


bfs(x)
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
