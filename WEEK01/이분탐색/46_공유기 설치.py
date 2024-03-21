# 2110

# 집과 집 사이의 거리를 돌면서 공유기를 설치할 거리
n, C = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[n - 1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    wh = house[0]  # 마지막으로 설치된 공유기의 위치

    for i in range(1,n):
        if house[i] - wh >= mid:  # 두번째로 설치할 공유기와 그전에 설치한 공유기간의 거리가 mid(공유기 간의 설치할 거리) 이상일경우->설치할 수 있음!!!
            count += 1  # 설치한 공유기 개수 추가
            wh = house[i]  # 마지막으로 설치된 공유기 위치 변경

    if count >= C:  # 공유기를 지금까지 설치 한 갯수가 설치해야 할 공유기 갯수 이상일 경우 공유기 간의 거리를 늘려야함(그래야 설치할 수 있는 공유기 갯수가 줄어듬)
        result = mid  # 일단 지금까지의 공유기 간의 설치한 최대 거리를 result에 담아둠
        start = mid + 1  # 시작지점을 처음 중앙값에서 더 큰쪽으로 옮김 (오른쪽)
    else:   # 공유기를 지금까지 설치 한 갯수가 설치해야할 공유기 갯수보다 적음 공유기 간의 거리를 줄여야함(그래야 설치할 수 있는 공유기 갯수가 늘어남
        end = mid -1
print(result)
