# 2630

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]  # 색종이
WHITE = 0
BLUE = 0


def recur(n, x, y):
    global WHITE, BLUE
    m = n // 2
    color = paper[x][y]  # 탐색 전 시작칸의 컬러
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:  # 시작색깔과 달라지는 순간 (분할 조건)
                recur(m, x, y)  # 1사분면
                recur(m, x, y + m)  # 2사분면
                recur(m, x + m, y)  # 3사분면
                recur(m, x + m, y + m)  # 4분면
                return
    if color == 0:
        WHITE += 1
    else:
        BLUE += 1

recur(n,0,0)
print(WHITE,BLUE)
