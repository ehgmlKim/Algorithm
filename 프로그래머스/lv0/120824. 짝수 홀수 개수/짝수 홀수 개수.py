def solution(num_list):
    cnt = 0
    for e in num_list:
        if e%2==0:
            cnt += 1
    return [cnt, len(num_list)-cnt]