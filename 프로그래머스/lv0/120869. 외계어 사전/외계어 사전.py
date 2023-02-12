def solution(spell, dic):
    answer = 2
    for e in dic:
        if sorted(spell) == sorted(e):
            answer = 1
    return answer