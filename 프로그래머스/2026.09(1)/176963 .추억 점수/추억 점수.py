def solution(name, yearning, photos):
    answer = []
    for photo in photos:
        result = 0
        for i in range(len(name)):
            result += yearning[i] * photo.count(name[i])
        answer.append(result)
    return answer