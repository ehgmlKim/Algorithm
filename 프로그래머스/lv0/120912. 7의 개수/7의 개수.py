def solution(array):
    answer = 0
    for e in array:
        answer += str(e).count('7')
    return answer