def solution(my_string):
    answer = 0
    for i in my_string:
        if ((i>='a' and i<='z') or (i>='A' and i<='Z')):
            pass
        else:
            answer += int(i)
    return answer