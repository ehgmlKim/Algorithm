def solution(n, lost, reserve):
    answer = 0
    dict = {}
    for l in lost:
        dict[l] = 0
    for r in reserve:
        dict[r] = 2
        
    for i in range(1, n+1):
        dict[i] = 1 # 원래 체육복은 1개씩 가지고 있다
        if i in reserve: #여분이 있다면 1개 더해준다
            dict[i] += 1
        if i in lost: # 잃어버렸다면 1개 빼준다
            dict[i] -= 1
        
    print(dict)
    for i in range(1, n+1):
        if i>1 and dict[i] == 0 and dict[i-1] == 2:
            dict[i] = 1
            dict[i-1] = 1
        if i<n and dict[i] == 0 and dict[i+1] == 2:
            dict[i] = 1
            dict[i+1] = 1
    print(dict)
    answer = len([x for x in dict.values() if x>0])   
    return answer