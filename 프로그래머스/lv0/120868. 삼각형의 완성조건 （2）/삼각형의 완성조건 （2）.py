def solution(sides):
    answer = 0
    old = max(sides)
    d = abs(sides[0] - sides[1])
    for i in range(d+1, old) : #원래가 가장 길 때
        answer += 1
    #새로운게 가장 길 때
    for i in range(old, sum(sides)) :
        answer += 1
    return answer