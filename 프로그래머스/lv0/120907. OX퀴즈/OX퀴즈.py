def solution(quiz):
    answer = []
    for e in quiz:
        if eval(e.split("=")[0]) == int(e.split("=")[1]) :
            answer.append("O")
        else:
            answer.append("X")
    return answer