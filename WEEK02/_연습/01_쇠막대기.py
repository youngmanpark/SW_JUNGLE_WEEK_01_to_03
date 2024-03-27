# 10799
arr=list(input())


answer=0

stack=[]
for i in range(len(arr)):
    if arr[i]=='(':
        stack.append(arr[i])
    else:
        if arr[i-1]=='(': # 레이저
            stack.pop()
            answer+=len(stack)
        elif arr[i-1]==')': #쇠막대기
            stack.pop()
            answer+=1

print(answer)