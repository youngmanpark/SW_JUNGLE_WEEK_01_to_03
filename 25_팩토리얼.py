#10872
import sys
sys.setrecursionlimit(10**6)
def factorial(n:int)->int:
    if n==0: return 1
    if n==1:return 1

    return n*factorial(n-1)
n=int(input())
print(factorial(n))