# 11663

n, m = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))


def left(line_L):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if dots[mid] < line_L:
            start = mid + 1
        else:
            end = mid - 1
    return start


def right(line_R):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if dots[mid] > line_R:
            end = mid - 1
        else:
            start = mid + 1

    return end


for line in lines:
    start1 = left(line[0])
    end1 = right(line[1])
    print(end1 - start1 + 1)





##############################################################################################
# def binary_search(start, end, target):
#
#     mid = (start + end) // 2
#     if start > end:
#         return 0
#     if mid == target:
#         return 1
#     elif mid < target:
#         start = mid + 1
#     elif mid > target:
#         end = mid - 1
#     return binary_search(start, end, target)
#
# for item in arr:
#     start=item[0]
#     end=item[1]
#     sum=0
#     for dot in dots:
#         sum+=binary_search(start,end,dot)
#     print(sum)
