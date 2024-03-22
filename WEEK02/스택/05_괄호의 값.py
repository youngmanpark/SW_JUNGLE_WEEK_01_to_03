# 2504

# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.
#
# 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
# 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
# X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.

# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.

# 첫번째! 괄호를 리스트로 하나씩 받아온다!
#
# 두번째! 괄호의 종류에 따라 각 다른 케이스를 둔다. '(' ')' '[' ']' 이렇게 4가지가 될 것!
#
# 세번째! 케이스를 나눈다!
# 세번째-1 ! ( 나 [ 와 같이 열린 괄호가 들어올 경우?!
#         2나 3을 한 변수에 곱해주고 (변수 초기값은 1. 0이면 아무리 곱해도 0이니까~)
#         올바른 괄호 판단 알고리즘대로 stack에 append 해준다.
# 세번째-2 ! )나 ] 와 같이 닫힌 괄호가 들어올 경우?! 일단 stack이 비지는 않았는지,
#         stack[-1]이 짝이 지어진 괄호가 맞는지 ('('의 짝은 ')', '['의 짝은 ']')를 먼저 체크한다.
#         여기서 틀리면 result=0 해주고 바로 break 🏳 ~! 맞으면 괄호가 닫혔으므로 2나 3을 다시 나눠주고, stack.pop() 해준다.
#
# 네번째! 닫힌괄호 앞의 괄호를 확인해보자!
#         세번째-2 전에 처리해줘야하는 과정이다.
#         만약에 닫힌 괄호가 들어왔고, 그 직전에 짝이 맞는 열린 괄호가 들어왔다면?
#         그 두 괄호는 쌍이 맞고 가장 안 쪽에 있으므로 애기 괄호가 된다. (예를 들면 () 또는 [] 순으로 들어왔을 때) 그럼 이 지점에서 result를 업데이트 해줘야 한다.
#         왜? 괄호의 한 케이스가 끝났으니까! 그니까 result += res 해줘버리자~

brackets = list(input())
stack = []
res = 1
result = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        res *= 2
        stack.append(brackets[i])

    elif brackets[i] == '[':
        res *= 3
        stack.append(brackets[i])
    elif brackets[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if brackets[i - 1] == '(':
            result += res
        res //= 2
        stack.pop()

    elif brackets[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if brackets[i - 1] == '[':
            result += res
        res //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
