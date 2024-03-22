# #2493

n= int(input())
top=list(map(int,input().split()))
stack=[]
answer=[0]*n

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]: #내 레이저를 받음
            answer[i] = stack[-1][0] + 1 #정답에 내레이저를 받은 탑의 인덱스+1 저장
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

print(*answer)