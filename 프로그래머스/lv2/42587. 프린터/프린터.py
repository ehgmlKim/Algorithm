def solution(priorities, location):
    prio = []
    answer = 0
    for i,p in enumerate(priorities):
        prio.append([i, p])
    
    while len(prio)>0:
        if prio[0][1] == max([x[1] for x in prio]) :
            answer += 1
            if prio[0][0] == location:
                break
            prio.remove(prio[0])
        else :
            prio.append([prio[0][0], prio[0][1]])
            prio.remove(prio[0])
            
    return answer