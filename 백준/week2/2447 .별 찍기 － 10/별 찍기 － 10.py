n = int(input())

result = [[" "]*n for _ in range(n)]

def draw_star(x, y, l):
    global result
    if l==3:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    result[x+i][y+j] = " "
                else:
                    result[x+i][y+j] = "*"
        return
    cnt = 0
    for a in range(x, x+l, l//3):
        for b in range(y, y+l, l//3):
            cnt += 1
            if cnt == 5:
                continue
            draw_star(a, b, l//3)

draw_star(0,0,n)
for i in range(n):
    print(''.join(result[i]))