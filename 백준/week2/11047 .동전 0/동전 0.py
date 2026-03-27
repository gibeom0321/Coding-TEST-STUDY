import sys
input = sys.stdin.readline

n, k = map(int, input().split())
change = []
result = 0

for i in range(n):
    change.append(int(input()))

for i in range(n-1, -1, -1):
    result += (k // change[i])
    k = (k % change[i])
    if k == 0:
        break

print(result)