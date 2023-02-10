def solution(s):
    answer = ''
    dic={}
    for e in sorted(s):
        if e not in dic:
            dic[e] = 1
        else :
            dic[e] += 1
    for k,v in dic.items() :
        if dic[k] == 1:
            answer+=k
    return answer