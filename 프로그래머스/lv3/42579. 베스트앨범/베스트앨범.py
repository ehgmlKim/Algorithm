def solution(genres, plays):
    answer = []
    dic={}
    for i in range(len(genres)) :
        if genres[i] not in dic:
            dic[genres[i]] = [(i, plays[i])]
        else:
            dic[genres[i]].append((i, plays[i]))
    
    play_count={}
    for i in range(len(genres)) :
        if genres[i] not in play_count :
            play_count[genres[i]] = 0
        play_count[genres[i]] += plays[i]
    for g,c in sorted(play_count.items(), key=lambda x:x[1], reverse=True):
        for i,p in sorted(dic[g], key=lambda x:x[1], reverse=True)[:2] :
            answer.append(i)
    return answer