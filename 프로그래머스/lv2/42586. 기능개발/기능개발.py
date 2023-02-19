def solution(progresses, speeds):
    answer = []
    days = []
    
    while len(progresses):
        count = 0
        while len(progresses) and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        if count:
            answer.append(count)
    return answer
            