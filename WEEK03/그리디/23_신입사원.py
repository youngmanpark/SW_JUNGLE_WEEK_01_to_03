# 1946
import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    n=int(input())
    score=[]
    for i in range(n):
        a,b=map(int,input().split())
        score.append([a,b])
    score.sort()

    count=1
    max_=score[0][1]
    for i in range(n):
        if max_>score[i][1]:
            count +=1
            max_=score[i][1]

    print(count)

