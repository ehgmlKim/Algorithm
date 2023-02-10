def solution(n):
    answer = 1
    min = n if n<6 else 6
    for i in range(1, min+1) :
        if 6%i==0 and n%i==0 :
            answer = i
    return n/answer