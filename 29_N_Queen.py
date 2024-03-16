#9663

def promising(col, i):
    k=1
    flag=True
    while k<i and flag:
        if col[i]==col[k] or abs(col[i]-col[k])==(i-k):
            flag=False
        k+=1
    return flag

def backtracking(i,col,count):#깊이가 i,컬럼이 col

    n=len(col)-1 #컬럼의 길이 -1( 0부터 시작하니까 )
    if promising(col,i): #깊이 i번째의 col가지고 유망한지 체크
        if i==n: #깊이가 끝까지 탐색했으면 더 내려갈곳이 없으면
            # print(col[1:n+1]) #col 1부터 n+1까지 반환
            count+=1
        else: #깊이가 다 안내려갔으면 다음 깊이 탐색
            for j in range(1,n+1):
                col[i+1]=j
                count=backtracking(i+1,col,count)
    return count

############################################################################################

def is_promising(col, i, j): #유망한지 확인하는 메소드
    for k in range(1, i):
        if col[k] == j or abs(col[k] - j) == abs(i - k): #같은 행이 아니고 대각선에 있을경우 false 더 이상 밑으로 트래킹 하지 않음
            return False
    return True

def queen(i, col, count): #i는 깊이 col은 배열 count는 정답트래킹 횟수
    n = len(col) - 1  # 0부터 시작하기 때문에 배열 길이의 -1
    if i > n: # 종료 조건 깊이 가변 변수 i가 아직 깊이 n(배열의 길이)보다 길어지는 순간
        return count + 1 #횟수 증가
    else:
        for j in range(1, n + 1):
            if is_promising(col, i, j):
                col[i] = j
                count = backtracking(i + 1, col, count)
    return count

n = int(input())
col = [0] * (n + 1)
print(queen(1, col, 0))
