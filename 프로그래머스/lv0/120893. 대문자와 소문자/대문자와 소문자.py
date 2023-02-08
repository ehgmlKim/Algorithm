def solution(my_string):
    answer = ''
    for e in my_string:
        if e>='a' and e<='z':
            answer+=e.upper()
        else:
            answer+=e.lower()
    return answer