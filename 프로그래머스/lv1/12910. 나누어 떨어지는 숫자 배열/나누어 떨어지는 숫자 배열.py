def solution(arr, divisor):
    answer = [x for x in sorted(arr) if x%divisor==0]
    if len(answer):
        return answer
    else:
        return [-1]