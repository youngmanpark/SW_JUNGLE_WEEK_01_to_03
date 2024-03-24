# 5639
import sys
sys.setrecursionlimit(10**9)
arr = []
while True:
    try:
        i = int(input())
        arr.append(i)
    except:
        break


def sol(arr):
    if len(arr) == 0:
        return
    Left,Right = [],[]

    root = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > root:
            Left = arr[1:i]
            Right = arr[i:]
            break
    else:
        Left = arr[1:]
    sol(Left)
    sol(Right)
    print(root)


sol(arr)
