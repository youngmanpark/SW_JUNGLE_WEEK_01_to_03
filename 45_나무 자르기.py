# 2805

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()


def cutting(height):
    length = 0
    for tree in trees:
        rest = tree - height
        if rest > 0:
            length += rest
    return length


def binary_search(start, end, target):
    if start > end: return end

    mid = (start + end) // 2

    if cutting(mid) >= target:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)


print(binary_search(0, max(trees) - 1, m))
