#9935
import sys
input = sys.stdin.readline

line=list(input().strip())
boom=input().strip()

stack=[]
for i in line:
    stack.append(i)

    if ''.join(stack[-len(boom):])==boom:
        for i in range(len(boom)):
            stack.pop()

s=''.join(stack)
if s:
    print(s)
else:
    print('FRULA')
