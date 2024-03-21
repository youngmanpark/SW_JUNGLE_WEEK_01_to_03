# 1920

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

arr.sort()


def binary_search(start, end, target):
    mid = (start + end) // 2
    if start > end:
        return 0
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        start = mid + 1
    elif arr[mid] > target:
        end = mid - 1
    return binary_search(start, end, target)


for target in targets:
    print(binary_search(0, len(arr) - 1, target))
