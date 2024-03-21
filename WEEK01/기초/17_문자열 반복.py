# 2675
# n = input()
# for i in range(int(n)):
#     a, b = input().split()
#     a = int(a)
#     b = list(b.strip())
#     arr = []
#     for j in b:
#         for k in range(a):
#             arr.append(j)
#     for j in arr:
#         print(j, end="")
t=int(input())
for _ in range(t):
    n,s=input().split()
    for i in s:
        print(i*int(n),end="")
    print()
