def solution(sides):    
    sides_list = sorted(sides)
    answer = 1 if sides_list[-1] < sides_list[0] + sides_list[1] else 2
    return answer