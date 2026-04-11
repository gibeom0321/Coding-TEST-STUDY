n = int(input())

def search_vps(vps):
    stack = []
    for i in vps:
        if i == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                return "NO"
            else: 
                stack.pop()
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

for i in range(n):
    v = input()
    print(search_vps(v))