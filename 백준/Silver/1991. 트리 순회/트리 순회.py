import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for i in range(n):
    a, b, c = input().split()
    dict[a] = [b, c]

def pre(n):
    if n == '.':
        return
    print(n, end = "")
    pre(dict[n][0])
    pre(dict[n][1])
    
def mid(n):
    if n == '.':
        return
    mid(dict[n][0])
    print(n, end = "")
    mid(dict[n][1])

def after(n):
    if n == '.':
        return
    after(dict[n][0])
    after(dict[n][1])
    print(n, end = "")

pre('A')
print()
mid('A')
print()
after('A')
    