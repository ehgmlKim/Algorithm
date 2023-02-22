def solution(d, budget):
    sum = 0
    count = 0
    d = sorted(d)
    for i in d:
        if sum+i<=budget:
            sum += i
            count += 1
    return count