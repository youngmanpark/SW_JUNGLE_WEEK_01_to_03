# 10971

##################################################################################
n = int(input())
W = []
for i in range(n):
    W.append(list(map(int, input().split())))
visited = [False] * n
path=[]
min_cost=float('inf')

visited = [0] * n
path = [0] * (n + 1)
cost_array = []
def get_cost(path):

    cost = 0
    for i in range(n+1):
        if i == n:
            cost += W[path[i]][path[0]]
        else:
            cost += W[path[i]][path[i + 1]]
    return cost_array.append(cost)


def dfs(depth):
    if depth == n:
        path[n] = path[0]
        get_cost(path)
        path[n]=0
        return
    for i in range(n):
        if visited[i] == 1: continue
        path[depth] = i
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0
        path[depth] = 0

######################################################################################

n = int(input())
W = []
for _ in range(n):
    W.append(list(map(int, input().split())))

visited = [False] * n
path = []
min_cost = float('inf')


def dfs(start, depth, cost):
    global min_cost

    if depth == n:
        # 모든 도시를 방문했을 때
        if W[start][path[0]] != 0:  # 시작 도시로 돌아갈 수 있는 경우만 계산
            min_cost = min(min_cost, cost + W[start][path[0]])
        return

    for next_city in range(n):
        if not visited[next_city] and W[start][next_city] != 0:
            visited[next_city] = True
            path.append(next_city)
            dfs(next_city, depth + 1, cost + W[start][next_city])
            visited[next_city] = False
            path.pop()


for start_city in range(n):
    visited[start_city] = True
    path.append(start_city)
    dfs(start_city, 1, 0)
    visited[start_city] = False
    path.pop()

print(min_cost)


