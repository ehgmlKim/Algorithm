def solution(age):
    answer = ''
    count = 0
    idx = []
    alpa='abcdefghijklmnopqrstuvwxyz'
    while age>0 :
        idx.insert(0, age%10)
        age = age // 10
    for i in idx:
        answer += alpa[i]
    return answer