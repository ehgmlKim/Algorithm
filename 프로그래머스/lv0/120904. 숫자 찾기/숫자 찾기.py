def solution(num, k):
    answer = 0
    num=str(num)
    k=str(k)
    try:
        answer = num.index(k)+1
    except:
        answer = -1
    return answer