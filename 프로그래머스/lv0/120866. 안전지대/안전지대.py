def solution(board):
    n = len(board)    
    move = ((-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1))

    answer = n**2
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for mx, my in move:
                    if not (0 <= i+mx < n and 0 <= j+my < n):
                        continue
                    if board[i+mx][j+my] == 1:
                        answer -= 1
                        break
            else:
                answer -= 1
              
    return answer