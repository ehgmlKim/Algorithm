def solution(n, numlist):
    answer = [e for e in numlist if e%n==0]
    
    return answer