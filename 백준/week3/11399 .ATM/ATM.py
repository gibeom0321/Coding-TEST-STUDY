import sys
input = sys.stdin.readline

n= int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0

l = len(arr)

for i in range(l):
    result += arr[i]*(l-i)
print(result)