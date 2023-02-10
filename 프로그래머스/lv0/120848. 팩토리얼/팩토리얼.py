def fact(n) :
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
def solution(n):
    answer = 0
    for i in range(1, 12) :
        if fact(i)>n :
            return i-1