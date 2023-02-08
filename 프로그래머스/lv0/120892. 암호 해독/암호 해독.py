def solution(cipher, code):
    answer = ''
    for i in range(-1, len(cipher), code):
        answer += cipher[i]
    return answer[1:]