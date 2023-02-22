def solution(n, m):
    min_v = min(n,m)
    max_v = max(n,m)
    for i in range(min_v, 0, -1):
        if max_v%i==0 and min_v%i==0:
            break
    answer = [i, min_v*max_v//i]
    return answer