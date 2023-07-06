def solution(clothes):
    dict = {}
    answer =1
    for a,b in clothes:
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = [a]
    for k,v in dict.items():
        answer *= len(v)+1
    return answer-1