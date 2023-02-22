def solution(s):
    answer = ''.join([x for x in sorted(s, reverse = True)])
    return answer