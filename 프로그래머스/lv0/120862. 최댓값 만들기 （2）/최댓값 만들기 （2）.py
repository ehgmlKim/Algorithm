def solution(numbers):
    answer = numbers[0]*numbers[1]
    for i in numbers:
        for j in numbers:
            if i != j :
                if i*j > answer :
                    answer = i*j
    return answer