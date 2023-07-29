from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while len(q)>1:
        if q[0] + q[-1]<=limit: # 둘이 같이 탈 수 있다면
            # 남아있는 사람 중에 제일 가벼운 사람 빼기
            q.popleft()
            # 남아있는 사람 중에 제일 무거운 사람 빼기
            q.pop()
        else:
            # 무거운 사람만 태우기
            q.pop()
        answer += 1

    if q:
        answer += 1
    return answer