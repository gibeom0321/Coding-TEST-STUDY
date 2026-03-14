import sys
input = sys.stdin.readline;

data = []
k, n = map(int, input().split())
for _ in range(k):
    data.append(int(input()))

def get_cnt(x):
    cnt = 0
    for i in range(k):
        cnt += data[i]//x
    return cnt

def lower_bound():
    start = 1
    end = max(data)
    ans = 0
    
    while start <= end:
        mid = (start + end) // 2
        if get_cnt(mid) >= n:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(lower_bound())