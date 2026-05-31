def solution(numbers, n):
    num_sum = 0
    for num in numbers:
        num_sum = num_sum + num
        if num_sum > n:
            return num_sum