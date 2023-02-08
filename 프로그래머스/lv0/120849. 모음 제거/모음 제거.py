def solution(my_string):
    answer = ''
    array = ['a', 'e', 'i', 'o', 'u']
    for e in my_string:
        if e not in array:
            answer += e
    return answer