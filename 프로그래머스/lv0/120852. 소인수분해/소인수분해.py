def solution(n):
    answer = []
    array=[]
    dic ={}
    for i in range(2, n+1) :
        dic[i] = 0
        for j in range(1,n+1):
            if i%j==0:
                dic[i] += 1
    for k,v in dic.items():
        if v==2:
            array.append(k)
    for e in array:
        if n%e==0:
            answer.append(e)
    return answer