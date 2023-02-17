from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices):
        now = prices.popleft()
        time = 0
        for x in prices:
            time += 1
            if x<now :
                break
            
        answer.append(time)
        
    return answer