def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = [] # 다리를 건너는 트럭
    time = {} # 각 트럭이 얼만큼 지났는지 표시하는 딕셔너리
    truck = list(enumerate(truck_weights))
    for t in truck:
        if t not in time:
            time[t] = 0 # 처음은 0으로 초기화
    while len(truck) :
        answer += 1 #경과 시간 
        # 다리를 다 건넌 트럭을 제거한다.
        ing = [x for x in ing if not time[x]==bridge_length]
        if sum([x[1] for x in ing])+truck[0][1]<=weight :
            ing.append(truck.pop(0))
        for i in ing:
            time[i] += 1 #시간이 지날때마다 1씩 증가
        #print(answer, ing, time) #확인용 프린트문

    while len(ing):
        answer += 1
        ing = [x for x in ing if not time[x]==bridge_length]
        for i in ing:
            time[i] += 1
        #print(answer, ing, time) #확인용 프린트문
    
    return answer