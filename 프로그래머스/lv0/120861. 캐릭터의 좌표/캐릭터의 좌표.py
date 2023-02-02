def solution(keyinput, board):
    move = {"up":(0, 1), "down":(0, -1),
            "left":(-1, 0), "right":(1, 0)}

    x, y = 0, 0
    
    for key in keyinput:
        move_x = x + move[key][0]
        move_y = y + move[key][1]
        width_max = board[0] // 2
        height_max = board[1] // 2

        if (-width_max <= move_x <= width_max) and (-height_max <= move_y <= height_max):
            x = move_x
            y = move_y
    
    return (x, y)