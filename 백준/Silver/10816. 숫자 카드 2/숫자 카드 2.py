import sys
input = sys.stdin.readline

n = int(input())
data_array = list(map(int, input().split()))
m = int(input())
check_array = list(map(int, input().split()))
result = []

def lower_bound(target):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if data_array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(target):
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if data_array[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start
            
data_array.sort()    
for i in range(len(check_array)):
    t = check_array[i]
    result.append(str(upper_bound(t) - lower_bound(t)))
print(' '.join(result))