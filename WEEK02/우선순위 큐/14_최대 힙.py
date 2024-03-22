#11279
import sys
import heapq

n=int(input())
arr=[]
for i in range(n):
    k=int(sys.stdin.readline())
    if k>0:
      heapq.heappush(arr,-k)
    else:
        if arr:
            max_value= -heapq.heappop(arr)
            print(max_value)
        else:
            print(0)
