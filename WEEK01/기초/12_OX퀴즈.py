# 8958
n = int(input())
str=[]
for i in range(n):
    str = list(input())
    p_num = 0
    result=0
    for item in str:
        if item == 'O':
            p_num+=1
            result+=p_num
        if item=='X':
            p_num=0
    print(result)