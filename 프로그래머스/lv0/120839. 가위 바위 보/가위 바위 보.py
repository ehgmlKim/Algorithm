def solution(rsp):
    answer=''
    for e in rsp:
        if e=='2':
            answer+='0'
        if e=='0':
            answer+='5'
        if e=='5':
            answer+='2'
    return answer