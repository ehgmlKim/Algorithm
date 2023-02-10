def solution(my_string):
    answer = ''
    my_string = list(my_string)
    for e in my_string :
        if e not in answer :
            answer += e
    return answer