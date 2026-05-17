def solution(myString):
    cnt = 0
    result = []
    for i in myString:
        if i == "x":
            result.append(cnt)
            cnt = 0
        else:
            cnt += 1
    result.append(cnt)
    return result