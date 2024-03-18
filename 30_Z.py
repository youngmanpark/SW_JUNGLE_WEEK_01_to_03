# 1074
import math


# n과 i,j가 주어진다
# (i,j)가 가장 큰경우에서 몇 사분면인지 체크한다 즉 큰덩어리 기준으로 몇번째로 갔는지
# 갈수록 작은덩어리로 몇번째인지 쭉 체크한다
# 체크 한 덩어리 큰거부터 작은순으로 2의 n승*2의 n승*사분면을 더해준다(큰거에서 작은거로 갈수록 n-i)

# def check_location(n, i, j):
#     box_n = math.pow(2, n)
#     if i < box_n / 2 and j < box_n / 2:
#         return 0 * box_n * box_n + check_location(n, i, j)
#     elif i < box_n / 2 and j < box_n:
#         return 1 * box_n * box_n + check_location(n, i, j)
#     elif i < box_n and j < box_n / 2:
#         return 2 * box_n * box_n + check_location(n, i, j)
#     elif i < box_n and j < box_n:
#         return 3 * box_n * box_n + check_location(n, i, j)


# 초기값


# def check(n, s1, d1, s2, d2, i, j):
#     if n > 0:
#         if s2 <= i and i < (s2 + d2) / 2 and s1 <= j and j < (s1 + d1) / 2:  # 1사분면
#             result = 0 * (int)(math.pow(2, n - 1) * math.pow(2, n - 1))
#             return result + check(n - 1, s1, (s1 + d1) / 2, s2, (s2 + d2) / 2, i, j)
#
#         if s2 <= i and i < (s2 + d2) / 2 and (s1 + d1) / 2 <= j and j < d1:  # 2사분면
#             result = 1 * (int)(math.pow(2, n - 1) * math.pow(2, n - 1))
#             return result + check(n - 1, (s1 + d1) / 2, d1, s2, (s2 + d2) / 2, i, j)
#
#         if (s2 + d2) / 2 <= i and i < d2 and s1 <= j and j < (s1 + d1) / 2:  # 3사분면
#             result = 2 * (int)(math.pow(2, n - 1) * math.pow(2, n - 1))
#             return result + check(n - 1, s1, (s1 + d1) / 2, (s2 + d2) / 2, d2, i, j)
#
#         if (s2 + d2) / 2 <= i and i < d2 and (s1 + d1) / 2 <= j and j < d1:  # 4사분면
#             result = 3 * (int)(math.pow(2, n - 1) * math.pow(2, n - 1))
#             return result + check(n - 1, (s1 + d1) / 2, d1, (s2 + d2) / 2, d2, i, j)
#     else:
#         return 0

def check(n, s1, d1, s2, d2, i, j):
    if n > 0:
        k = (int)(math.pow(2, n - 1))
        if i < (s2 + d2) / 2 and j < (s1 + d1) / 2:  # 1사분면
            result = 0 * k * k
            return result + check(n - 1, s1, (s1 + d1) / 2, s2, (s2 + d2) / 2, i, j)

        elif i < (s2 + d2) / 2 and j < d1:  # 2사분면
            result = 1 * k * k
            return result + check(n - 1, (s1 + d1) / 2, d1, s2, (s2 + d2) / 2, i, j)

        elif i < d2 and j < (s1 + d1) / 2:  # 3사분면
            result = 2 * k * k
            return result + check(n - 1, s1, (s1 + d1) / 2, (s2 + d2) / 2, d2, i, j)

        elif i < d2 and j < d1:  # 4사분면
            result = 3 * k * k
            return result + check(n - 1, (s1 + d1) / 2, d1, (s2 + d2) / 2, d2, i, j)
    else:
        return 0


n, i, j = map(int, input().split())
s1, s2 = 0, 0
d1, d2 = math.pow(2, n), math.pow(2, n)
print(check(n, s1, d1, s2, d2, i, j))
