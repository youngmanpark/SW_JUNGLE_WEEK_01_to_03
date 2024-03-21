#2908
a,b=input().split()

a=list(a)
a.reverse()
b=list(b)
b.reverse()

str1=""
str2=""
for i in a:
    str1+=i
for i in b:
    str2+=i
result=int(str1) if int(str1)>int(str2) else int(str2)
print(result)