def solution(t, p):
    answer = 0
    l = len(t)
    len_p = len(p)
    for i in range(l-len_p+1):
        if int(t[i:i+len_p])<=int(p):
            answer += 1
    return answer