# # deque 라이브러리 불러오기
# from collections import deque
#
#
# # BFS 메서드 정의
# def bfs(graph, node, visited):
#     # 큐 구현을 위한 deque 라이브러리 활용
#     queue = deque([node])
#     # 현재 노드를 방문 처리
#     visited[node] = True
#
#     # 큐가 완전히 빌 때까지 반복
#     while queue:
#         # 큐에 삽입된 순서대로 노드 하나 꺼내기
#         v = queue.popleft()
#         # 탐색 순서 출력
#         print(v, end=' ')
#         # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# graph = [
#     [],
#     [2, 3],
#     [1, 8],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7, 8],
#     [6, 8],
#     [2, 6, 7]
# ]
#
# # 노드별로 방문 정보를 리스트로 표현
# visited = [False] * 9
#
# # 정의한 BFS 메서드 호출(노드 1을 탐색 시작 노드로 설정)
# bfs(graph, 1, visited)

from collections import deque
import copy


def solution(maps):
    maps_2 = copy.deepcopy(maps)
    n = len(maps)  # y축
    m = len(maps[0])  # x축
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = deque([[0, 0, 1]])
    for i in range(n):
        for j in range(m):
            maps_2[i][j] = 0
    visit = maps_2
    visit[0][0] = True

    while stack:
        node = stack.popleft()
        print(node)
        if node[0] == n - 1 and node[1] == m - 1:
            return node[2]
        for i in range(4):
            xx = dx[i] + node[0]  # y축
            yy = dy[i] + node[1]  # x축
            if 0 <= xx < n and 0 <= yy < m and not visit[xx][yy] and maps[xx][yy] == 1:
                visit[xx][yy] = True
                stack.append([xx, yy, node[2] + 1])

    return -1
#시작 지점이 2, 종점이 3인 미로를 종점까지의 거리 탐색하는 코드
def bfs(a, b):
    visited = [[0] * N for _ in range(N)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # ->,<-,v,^
    queue = []
    queue.append([a, b])  # 큐에 초기값 지정
    visited[a][b] = 1  # 초기값 1
    while queue:
        y, x = queue.pop(0)
        if maze[y][x] == 3:
            return visited[y][x] - 2  # 도착지점 기준 시작값 1과 끝값 1을 뺴줘야함
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            # 범위 밖을 벗어나지 않으면서 1이 아니고, 방문하지 않았을 경우
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])
    return 0

N = 5
maze = [[1,1,2,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,0,3]]
print(bfs(0,2))

# 출력 결과 6