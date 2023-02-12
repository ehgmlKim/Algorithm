def solution(clothes):
    dic = {}
    answer = 1
    for e in clothes :
        if e[1] not in dic:
            dic[e[1]] = 1
        else :
            dic[e[1]] += 1
    for v in dic.values() :
        answer *= (v+1)
    return answer-1