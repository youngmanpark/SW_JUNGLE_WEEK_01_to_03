#17608

n=int(input())
stack=[]
for i in range(n):
    number=int(input())


    if stack:
        if stack[-1]>number:
            stack.append(number)
        else:
            while stack and stack[-1]<=number:
                stack.pop()
            stack.append(number)
    else:
        stack.append(number)

print(len(stack))