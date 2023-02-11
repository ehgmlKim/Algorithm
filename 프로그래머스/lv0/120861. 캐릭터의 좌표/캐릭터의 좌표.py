def solution(keyinput, board):
    answer = [0, 0]
    for e in keyinput:
        if e == "right" :
            answer[0] = answer[0]+1 if answer[0]+1<=board[0]//2 else answer[0]
        elif e == "left" :
            answer[0] = answer[0]-1 if answer[0]>=1-board[0]//2 else answer[0]
        elif e == "up" :
            answer[1] = answer[1]+1 if answer[1]+1<=board[1]//2 else answer[1]
        else :
            answer[1] = answer[1]-1 if answer[1]>=1-board[1]//2 else answer[1]
    return answer