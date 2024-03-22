#9012

n=int(input())

for i in range(n):
    arr=input()
    flag=True
    check=[]
    for item in arr:

        if item =='(':
            check.append(item)
        elif item ==')':
            if check and check[-1]=='(':
                check.pop()
            else:
                flag=False
                break

    if not check and  flag:
        print("YES")
    else:
        print("NO")