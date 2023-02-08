def solution(array, n):
    answer = 0
    for e in array:
        if e == n:
            answer += 1
    return answer