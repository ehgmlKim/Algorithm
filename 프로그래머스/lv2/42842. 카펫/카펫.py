def solution(brown, yellow):
    answer = []
    for i in range(3, (brown-2)//2+1):
        h = (brown-i*2)//2
        if yellow == (i-2) * h:
            answer.append((brown+yellow)//i)
            answer.append(i)
            
            break
    
    return answer