def solution(board):
    answer = []
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] == 1 :
                answer.append((i, j))
                answer.append((i, j+1))
                answer.append((i, j-1))
                answer.append((i-1, j))
                answer.append((i+1, j))
                answer.append((i+1, j+1))
                answer.append((i-1, j-1))
                answer.append((i+1, j-1))
                answer.append((i-1, j+1))
    
    answer = [i for i in set(answer) if 0<=i[0]<len(board) and 0<=i[1]<len(board)]
    
    return len(board)**2 - len(answer)