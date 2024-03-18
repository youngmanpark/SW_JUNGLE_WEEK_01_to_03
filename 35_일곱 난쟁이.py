# 2309

arr = []
for i in range(9):
    arr.append(int(input()))
path = [0] * 7


def dfs(level, start):
    # 7장 모두 뽑았으면 출력하고 리턴
    if level == 7:
        if sum(path) == 100:
            for i in sorted(path):
                print(i)
            exit()
        else :
            return


    for i in range(start, 9):
        path[level] = arr[i]
        dfs(level + 1, i + 1)
        path[level]=0


dfs(0, 0)
