def solution(genres, plays):
    answer = []
    cnt = {}
    top = {}
    for i, (g,p) in enumerate(zip(genres, plays)):
        if g not in cnt:
            cnt[g] = p
        else:
            cnt[g] += p
        
        if g not in top:
            top[g] = [(i, p)]
        else:
            top[g].append((i, p))
    
    for (k,v) in sorted(cnt.items(), key = lambda x : x[1], reverse = True):
        for (i, p) in sorted(top[k], key = lambda x : x[1], reverse = True)[:2]:
            answer.append(i)
    return answer