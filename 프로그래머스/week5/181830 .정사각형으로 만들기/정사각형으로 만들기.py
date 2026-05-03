def solution(arr):
    column = len(arr)
    row = len(arr[0])
    
    if column > row:
        for i in arr:
            for j in range(column-row):
                i.append(0)
    if row > column:
        for i in range(row-column):
            arr.append([0]*(row))
    return arr