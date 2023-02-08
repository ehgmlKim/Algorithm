def solution(s1, s2):
    answer = 0
    for e in s1:
        if e in s2:
            answer+=1
    return answer