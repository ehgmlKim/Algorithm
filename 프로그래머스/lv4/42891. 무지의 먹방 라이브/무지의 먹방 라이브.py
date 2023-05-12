
2
3
4
5
6
7
8
9
10
11
12
13
def solution(food_times, k):
    if k>=sum(food_times):return -1
    times_sorted = sorted([(idx, val) for idx, val in enumerate(food_times)], key=lambda x: x[1])
    t = idx = 0
    n = len(food_times)
    cycle = times_sorted[0][1]
    while k-(n*cycle)>0:
        k -= n*cycle
        n -= 1
        idx += 1
        cycle = times_sorted[idx][1]-times_sorted[idx-1][1]
    return [i[0]+1 for i in sorted(times_sorted[idx:])][k%n]
