#1655
import heapq
import sys


n= int(sys.stdin.readline())
L_heap=[]
R_heap=[]

for i in range(n):
    num= int(sys.stdin.readline())

    if len(L_heap)==len(R_heap):
        heapq.heappush(L_heap,-num)
    else:
        heapq.heappush(R_heap,num)
    if R_heap and R_heap[0]<-L_heap[0]:
        L_value=-heapq.heappop(L_heap)
        R_value=-heapq.heappop(R_heap)

        heapq.heappush(L_heap,R_value)
        heapq.heappush(R_heap,L_value)

    print(-L_heap[0])
