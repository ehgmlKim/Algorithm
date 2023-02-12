def solution(score):
    answer = []
    rank=[]
    for e in score:
        rank.append(sum(e))
    rank = sorted(rank, reverse = True)
    rank_dic={}
    for i in rank:
        rank_dic[i] = rank.index(i)+1
    for e in score:
        answer.append(rank_dic[sum(e)])
    return answer