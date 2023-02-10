def solution(s):
    answer=0
    arr= s.split()
    idx=[]
    for e in range(len(arr)):
        if arr[e] == 'Z':
            idx.append(e)
    for i in range(len(arr)):
        if i not in idx:
            answer += int(arr[i])
        if i in idx:
            answer -= int(arr[i-1])
    return answer