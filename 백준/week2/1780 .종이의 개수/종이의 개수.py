import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
check_0 = 0
check_1 = 0
check_minus1 = 0

def check(x, y, l):
    global check_0
    global check_1
    global check_minus1
    first = graph[x][y]
    
    for i in range(l):
        for j in range(l):
            if first != graph[x+i][y+j]:
                return True
    if first == 1:
        check_1 += 1
    elif first == 0:
        check_0 += 1
    else:
        check_minus1 += 1
    return False

def devide(x, y, l):
    if check(x, y, l):
        l //= 3
        for i in range(3):
            for j in range(3):
                devide(x+i*l, y+j*l, l)
    else:
        return
devide(0, 0, n)
print(check_minus1)
print(check_0)
print(check_1)