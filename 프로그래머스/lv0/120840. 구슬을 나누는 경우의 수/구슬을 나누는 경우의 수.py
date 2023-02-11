def fac(n) :
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)
def solution(balls, share):
    answer = fac(balls)/fac(balls-share)/fac(share)
    return answer