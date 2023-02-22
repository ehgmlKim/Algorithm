def solution(n):
    answer = 0
    for i in range(2, n+1):
        result = True
        for j in range(2, int(i**(1/2))+1):
            if i%j==0 and i!=j:
                result = False
                break
        if result:
            answer += 1
        
    return answer