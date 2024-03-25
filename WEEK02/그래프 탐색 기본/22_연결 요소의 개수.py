# 11724
import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#순서 반환이 아니기때문에 굳이 부모노드의 자식노드들에 대한 오름차순 정렬 필요가 없음
# for i in graph:
#     i.sort()

visited=[False]*(n+1)

def dfs(start):
     visited[start]=True
     for i in graph[start]:
         if not visited[i]:
             dfs(i)
count=0
for i in range(1,n+1):
    if not visited[i]:
        count+=1
        dfs(i)

print(count)