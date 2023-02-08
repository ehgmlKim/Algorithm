def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    answer = numbers[len(numbers)-1]*numbers[len(numbers)-2]
    return answer