def solution(players, callings):
    answer = []
    play = {}
    rank = {}
    for i, p in enumerate(players):
        play[p] = i
        rank[i] = p
    
    for c in callings:
        # now 현재 등수
        now = play[c]
        rank[now] = rank[now-1]
        rank[now-1] = c
        play[rank[now]], play[rank[now-1]] = play[rank[now-1]], play[rank[now]]
        
    rank = sorted(rank.items(), key = lambda x : x[0])
    answer = [x[1] for x in rank]
    return answer