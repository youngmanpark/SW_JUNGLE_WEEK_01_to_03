# 1085
x, y, w, h = input().split()

list = []
list=[int(x), int(y), abs(int(x) - int(w)), abs(int(y) - int(h))]
list.sort()
print(list[0])
