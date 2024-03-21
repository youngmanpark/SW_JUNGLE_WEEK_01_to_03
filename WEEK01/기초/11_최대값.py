#2562
list=[]
for i in range(9):
    list.append(int(input()))
max=0
max_n=0
for i in range(0,9):
    if(list[i]>max):
        max=list[i]
        max_n=i
print(max)
print(max_n+1)