# 1916
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

distance = [float('inf')] * (n + 1)
visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    distance[start] = 0
    visited[start] = True
    while q:
        now = q.popleft()
        visited[now] = False
        for next_node, next_cost in graph[now]:
            if distance[next_node] > distance[now] + next_cost:
                distance[next_node] = distance[now] + next_cost
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

bfs(start)
print(distance[end])