# 2577
a, b, c = input(), input(), input()

result = str((int(a) * int(b) * int(c)))

arr = list(result)

num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for n in arr:
    if n == '1':
        num[1] += 1
    if n == '2':
        num[2] += 1
    if n == '3':
        num[3] += 1
    if n == '4':
        num[4] += 1
    if n == '5':
        num[5] += 1
    if n == '6':
        num[6] += 1
    if n == '7':
        num[7] += 1
    if n == '8':
        num[8] += 1
    if n == '9':
        num[9] += 1
    if n == '0':
        num[0] += 1
for i in num:
    print(i)
