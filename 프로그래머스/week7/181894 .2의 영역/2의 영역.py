def solution(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            start_index = i
            for j in range(len(arr)-1,-1,-1):
                if arr[j] == 2:
                    end_index = j
                    return arr[start_index:end_index+1]
    return [-1]