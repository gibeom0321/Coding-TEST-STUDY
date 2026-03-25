import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
data = [list(input().strip()) for _ in range(n)]

def quard(x, y, l):
    check = data[x][y]
    for i in range(l):
        for j in range(l):
            if data[x+i][y+j] != check:
                l //= 2
                print("(", end = "")
                quard(x, y, l)
                quard(x, y+l, l)
                quard(x+l, y, l)
                quard(x+l, y+l, l)
                print(")", end = "")
                return
    print(data[x][y], end= "")
quard(0, 0, n)
    