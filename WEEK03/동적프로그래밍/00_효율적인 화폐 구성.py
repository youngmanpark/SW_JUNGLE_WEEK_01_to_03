n,m= map(int,input().split())

array=[]
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d= [10001]*(m+1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0]=0 # 아무것도 사용안해도 만들 수 있는 금액(0원)
for i in range(n): # i는 각각의 화폐 단위
    for j in range(array[i],m+1): # j는 각각의 금액(모든 금액 확인)

        # 현재 금액에서 현재 확인하고 있는 화폐 단위의 금액을 뺸 그 금액을 만들 수 있다면
        if d[j-array[i]]!=10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[j],d[j-array[i]]+1)

# 계산된 결과 출력
if d[m]==10001: print(-1)
else: print(d[m])
