from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    for p, s in zip(progresses, speeds):
        days.append((100-p)//s + (0 if (100-p)%s == 0 else 1))
    print(days)
    cnt = 1
    d = days.popleft()
    while len(days)>0:
        if days[0] <= d:
            days.popleft()
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 0
            d = days[0]
    answer.append(cnt)
    return answer