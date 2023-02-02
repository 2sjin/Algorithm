def solution(food):
    
    answer = ""
    for i in enumerate(i//2 for i in food):
        answer += str(i[0]) * i[1]
    
    return answer + "0" + answer[-1::-1]