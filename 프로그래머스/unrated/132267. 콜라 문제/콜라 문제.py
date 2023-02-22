def solution(a, b, n):
    answer = (n//a)*b
    n = n%a + answer
    while n>0:
        if n<a:
            break
        else:
            answer += (n//a)*b
            n = n%a + (n//a)*b
    return answer