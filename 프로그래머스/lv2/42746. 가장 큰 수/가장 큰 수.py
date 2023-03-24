def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=lambda x : str(x)*4, reverse = True)
    #print(numbers)
    for n in numbers:
        answer += str(n)
    return str(int(answer))
    