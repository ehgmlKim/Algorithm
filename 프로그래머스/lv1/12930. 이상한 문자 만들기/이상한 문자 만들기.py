def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if (i-cnt)%2==0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        else:
            cnt = i+1
            answer += ' '
        
    return answer