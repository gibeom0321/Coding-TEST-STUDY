import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

com_list = a+b
com_list.sort()
com_list = map(str, com_list)

print(' '.join(com_list))