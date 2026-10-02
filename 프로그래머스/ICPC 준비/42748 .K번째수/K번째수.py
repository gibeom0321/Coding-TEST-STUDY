def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        slice_array = array[i-1:j]
        slice_array.sort()
        answer.append(slice_array[k-1])
    return answer