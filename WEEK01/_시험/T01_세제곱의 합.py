#28701

n=int(input())
sum_1=0
sum_2=0
sum_3=0
for i in range(1,n+1):
    sum_1+=i

for i in range(1,n+1):
    sum_3+=i*i*i
print(sum_1)
print(sum_1*sum_1)
print(sum_3)