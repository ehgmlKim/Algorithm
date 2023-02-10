def solution(before, after):
    dic={}
    answer = 0
    for e in before :
        if e not in dic :
            dic[e] = 1
        else :
            dic[e] += 1
    for e in after :
        if e in dic :
            dic[e] -= 1
    for val in dic.values() :
        if val != 0:
            answer += 1
    answer = 1 if answer == 0 else 0
    return answer 