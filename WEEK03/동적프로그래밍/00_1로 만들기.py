# 정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# x가 5로 나누어 떨어지면, 5로 나눈다.
# x가 3으로 나누어 떨어지면, 3으로 나눈다.
# x가 2로 나누어 떨어지면, 2로 나눈다.
# x에 서 1을 뺀다.
# 정수 x가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.
# 1. 26-1 = 25
# 2. 25/5 = 5
# 3. 5/5 = 1

import sys
input = sys.stdin.readline

N = int(input())
mem = [0]*(N+1) # 연산 횟수 메모이제이션
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1"

for idx in range(2, N+1):
    mem[idx] = mem[idx-1] + 1
    prev = idx-1
    if idx % 3 == 0 and mem[idx//3]+1 < mem[idx]:
        mem[idx] = mem[idx//3] + 1
        prev = idx // 3
    if idx % 2 == 0 and mem[idx//2]+1 < mem[idx]:
        mem[idx] = mem[idx//2] + 1
        prev = idx // 2
    path[idx] = str(idx) + " " + path[prev]

print(mem[N])
print(path[N])