def yaksu(n) :
    answer = []
    i=1
    while i<=n :
        if n%i == 0:
            answer.append(i)
            n = n//i
            i=1
        i = i+1
    return answer
def solution(a, b):
    answer = 1
    yak_a = yaksu(a)
    yak_b = yaksu(b)
    dic = {}
    for e in yak_b:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    for e in yak_a:
        if e in dic:
            dic[e] -= 1
    for k,v in dic.items() :
        if k not in [2,5] and v > 0:
            return 2
    return answer