import sys
input = sys.stdin.readline

n = int(input())
arr = []
plus_arr = []
minus_arr = []
result = 0

for _ in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    a = arr.pop()
    if a > 1:
        plus_arr.append(a)
    elif a == 1:
        result += 1
    else:
        minus_arr.append(a)

def bind(x):
    global result
    l = len(x)
    for i in range(0, l-1, 2):
        result += x[i] * x[i+1]
    if l % 2 == 1:
        result += x[-1]
    return
bind(plus_arr)
minus_arr.sort()
bind(minus_arr)


print(result)