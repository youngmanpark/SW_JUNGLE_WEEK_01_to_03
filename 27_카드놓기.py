# 5568
# 여기가 이제 n개에서 k개를 순서 상관 없이 뽑기
"""
def backtracking(x):
    if 정답:
    	출력/저장
    else:
    	for 자식노드:
            if 자식노드가 유망한지(promising): 유망하면
            	자식노드로 이동
                backtracking(x+1)
                부모노드로 이동
"""

def dfs(depth):
    if depth == k: #깊이가 k가 되었을 때
        set_list.add(''.join(li))
        return
    for i in range(n): #n번 반복
        if check[i]==1:
            continue
        li.append(card[i])
        check[i]=1
        dfs(depth+1)
        li.pop()
        check[i]=0

n, k = int(input()), int(input())
card = []  # n개의 카드가 담겨있는 리스트
set_list = set()  # n개의 카드중 k를 뽑아서 순서상관없이 넣을 리스트 추후 중복제거(set 사용)
li=[]
for i in range(n):
    card.append(str(input()))

check=[0]*n

dfs(0)

print(len(set_list))
