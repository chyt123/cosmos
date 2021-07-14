

def my_sqrt(n):
    # neg: Raise error, >=0
    if n < 0:
        raise RuntimeError('input must >= 0.')
    if n < 2:
        return n

    l, r = 0, n  # [)
    mid = 0
    flag = False
    while l < r:
        mid = (l + r) // 2
        if mid ** 2 == n:
            return mid
        if mid ** 2 > n:
            r = mid
            flag = True
        else:
            l = mid + 1
            flag = False
    return mid - 1 if flag else mid


test_cases = [
    -1,
    0,
    1,
    9,
    13,
]
# for i in test_cases:
for i in range(26):
    # my_sqrt(i)
    print(i, my_sqrt(i))
