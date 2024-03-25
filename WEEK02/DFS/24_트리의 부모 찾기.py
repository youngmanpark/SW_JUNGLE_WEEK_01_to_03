#11725
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(n+1)]
result=[0]*(n+1)

def dfs(start):
    visited[start]=True

    for i in graph[start]:
        if not visited[i]:
            result[i]=start

            dfs(i)
dfs(1)

for i in range(2,len(result)):
    print(result[i])