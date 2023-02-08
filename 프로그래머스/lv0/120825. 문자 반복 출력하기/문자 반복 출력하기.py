def solution(my_string, n):
    answer = ''
    for e in my_string:
        for i in range(n):
            answer += e
    return answer