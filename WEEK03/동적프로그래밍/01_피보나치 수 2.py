# 2748
# 디피는 기본적으로 배열을 잘 활용해야 하는듯?
# 배열에 넣어두고 꺼내면서 확인?
n=int(input())

fibo=[]
fibo.append(0)
fibo.append(1)

for i in range(2,n+1):
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n])

