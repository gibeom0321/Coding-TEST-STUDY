import sys
input = sys.stdin.readline

n = int(input())
data_array = list(map(int, input().split()))
m = int(input())
check_array = list(map(int, input().split()))
result = []
data_array.sort()

def binary_search(x):
    start = 0
    end = len(data_array)-1
    while start <= end:
        mid = (start + end) // 2
        if data_array[mid] == x:
            result.append('1')
            return
        elif data_array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    result.append('0')
    return
for i in range(len(check_array)):
    binary_search(check_array[i])

print(' '.join(result))