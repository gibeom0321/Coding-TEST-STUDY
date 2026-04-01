import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])
data.sort(key = lambda x: (x[1], x[0]))

def search(n):
    a, b = data[0][0], data[0][1]
    cnt = 1
    for i in range(1, n):
        x, y = data[i][0], data[i][1]
        if b <= x:
            a, b = x, y
            cnt += 1
    return cnt

print(search(n))
    