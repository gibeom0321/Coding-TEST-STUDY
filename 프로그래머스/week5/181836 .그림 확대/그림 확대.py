def solution(picture, k):
    result =[]
    for row in picture:
        expended_row = ''.join(char*k for char in row)
        for _ in range(k):
            result.append(expended_row)
        
    return result