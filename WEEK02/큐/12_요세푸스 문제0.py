# # 11866
# from collections import deque
#
# n, k = map(int, input().split())
# arr = deque()
# for i in range(n):
#     arr.append(i + 1)
# result = []
# while len(arr) >= k:
#     for i in range(len(arr)):
#         if i == k-1:
#             result.append(arr.popleft())
#             break
#         arr.append(arr.popleft())
# if len(arr) < k:
#     for i in range(len(arr)):
#         result.append(arr[(len(arr)+1+i)%k])
#
#
# print("<",end="")
# print(result[0],end="")
# for i in range(1,len(result)):
#     print(",",result[i],end="")
# print(">")

from collections import deque

n, k = map(int, input().split())
arr = deque()
for i in range(1, n + 1):
    arr.append(i)

result = []
while arr:
    arr.rotate(-(k - 1))
    result.append(arr.popleft())

print("<", end="")
print(*result, sep=", ", end="")
print(">")