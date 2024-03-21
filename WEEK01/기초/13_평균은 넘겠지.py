#4344
c=int(input())

for i in range(c):
    v=input().split()
    n=int(v[0])
    arr=[int(i) for i in v[1:]]
    sum=0
    for i in range(n):
        sum+=arr[i]
    arrange=sum/n
    over=0;
    for i in arr:
        if i>arrange:
            over+=1
    print("{:.3f}".format(over/n*100),"%")


