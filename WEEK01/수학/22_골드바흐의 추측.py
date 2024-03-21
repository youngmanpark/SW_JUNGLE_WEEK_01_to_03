# 9020
import math

def d(N):  # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True


N = int(input())  # 테스트 케이스 수 입력

for _ in range(N):
    num = int(input())  # 짝수 입력

    A = num // 2  # 두 수 중 줄어드는 변수
    B = num // 2  # 두 수 중 늘어나는 변수

    for _ in range(num // 2):
        if d(A) and d(B):  # 두 수가 소수이면 출력
            print(A, B)
            break
        else:  # 소수가 아니면 두 수를 줄이고 늘리기
            A -= 1
            B += 1
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     arr = []
#     for i in range(1, n - 1):
#         arr.append(i + 1)
#     for i in range(2, int(n / 2) + 1):
#         for j in range(i, int(n / 2) + 1):
#             if arr.count(i * j) > 0:
#                 arr.remove(i * j)
#     print(arr)
#
#     # a,b=0,0
#     # max=n
#     # for i in arr:
#     #     for j in arr:
#     #         if(i+j)==n and max>abs(i-j):
#     #             max=abs(i-j)
#     #             a=i
#     #             b=j
#
#     a,b=n//2,n//2
#     while a>0:
#         if a in arr and b in arr:
#             print(a,b)
#             break
#         else:
#             a-=1
#             b+=1
#

