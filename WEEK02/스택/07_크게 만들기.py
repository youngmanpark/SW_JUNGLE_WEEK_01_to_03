#2812

n, k=map(int, input().split())
number=list(map(int,input()))

stack=[]
count=0
for i in range(n):

    # 없으면 일단 넣기
    if stack:
        #스택의 맨뒤와 다음에 올숫자 비교해서 다음에 올 숫자가 크면 pop
        if stack[-1]<number[i]:
            while count<k and stack:
                if stack[-1]<number[i]:
                    stack.pop()
                    count+=1
                else:
                    break
            stack.append(number[i])

        else:
            stack.append(number[i])
    else:
        stack.append(number[i])
stack=stack[:n-k]
ans=''
for char in stack:
    ans+=str(char)
print(ans)
