import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

def cutting(x):
    result = 0
    for i in data:
        cut = i-x
        if cut >= 0:
            result += cut
    return result

def parametric_search():
    start, end = 1, max(data)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if cutting(mid) >= m:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(parametric_search())
            