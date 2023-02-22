def solution(s, n):
    answer = ''
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*2
    a = "abcdefghijklmnopqrstuvwxyz"*2
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                idx = A.find(s[i])
                answer += A[idx+n]
            else:
                idx = a.find(s[i])
                answer += a[idx+n]
        else:
            answer += ' '
    return answer