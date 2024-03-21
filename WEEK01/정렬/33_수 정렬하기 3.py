#10989

import sys
import sys

# 입력 받기
n = int(input())
arr = [0] * 10001

# 숫자 등장 횟수 세기
for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

# 등장 횟수대로 출력하기
for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            print(i)