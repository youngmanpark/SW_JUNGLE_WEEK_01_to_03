#1181
from collections import defaultdict

n= int(input())
arr={}
for i in range(n):
    a=input()
    arr[a]= len(a)

sort_arr = defaultdict(list)

for i in arr:
    sort_arr[arr[i]].append(i)

for i in range(51):
    if sort_arr[i]:
        sort_arr[i].sort()
        for alpha in sort_arr[i]:
            print(alpha)

