# 2588
a = int(input())
b = input()

result = a*int(b)

list=[]
for i in reversed(b):
    list.append(i)

for i in range(len(list)):
    print(a * int(list[i]))
print(result)
