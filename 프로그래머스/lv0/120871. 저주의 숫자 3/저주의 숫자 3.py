def solution(n):
    answer = []
    i=1
    while len(answer)<101 :
        if i%3 != 0 and '3' not in str(i):
            answer.append(i)
        i += 1
    return answer[n-1]