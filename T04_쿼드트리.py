#1992

#전체가 0 1 될때까지 돌기(분할 들어가기)

# 일단 먼저 4분할 하고 각각의 분면이 0, 1, 섞여있는지 체크 하는 함수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
video = []
for _ in range(n):
    v = [int(x) for x in list(input().rstrip())]
    video.append(v)

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)

    if s == n ** 2:
        return '1'
    if s == 0:
        return '0'

    half = n // 2
    temp = '('
    temp += quadtree(half, [l[:half] for l in vlist[:half]])
    temp += quadtree(half, [l[half:] for l in vlist[:half]])
    temp += quadtree(half, [l[:half] for l in vlist[half:]])
    temp += quadtree(half, [l[half:] for l in vlist[half:]])
    temp += ')'

    return temp


print(quadtree(n, video))
