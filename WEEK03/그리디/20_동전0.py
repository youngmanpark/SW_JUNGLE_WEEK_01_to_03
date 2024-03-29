# 11047
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
count=0
for i in range(n):
    count+=k//arr[n-1-i]
    k%=arr[n-1-i]
print(count)