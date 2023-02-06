def solution(lottos, win_nums):
    answer = [7, 7]

    for i in lottos:
        if i in win_nums:
            answer[0] -= 1

    answer[1] = answer[0] 
    answer[0] -= lottos.count(0)
    
    answer[0] = 6 if answer[0] == 7 else answer[0]
    answer[1] = 6 if answer[1] == 7 else answer[1]
    
    return answer