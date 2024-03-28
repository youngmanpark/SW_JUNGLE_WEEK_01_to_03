# 1766
import heapq
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1



# 먼저 푸는것이 좋은 문제 반드시 먼저 풀어야한다. 이조건 체크 어케하지=> 우선순위 큐!~!
def bfs():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:  # 차수가 적은것을 먼저 큐에 넣기
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:  # 큐에 들어간 노드와 연결된 즉 차수 높은 놈들
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
    for i in result:
        print(i, end=' ')


bfs()