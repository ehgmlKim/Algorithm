def solution(i, j, k):
    answer = ''
    for e in range(i, j+1) :
        answer += str(e)
    return answer.count(str(k))