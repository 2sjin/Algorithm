def solution(s):

    answer = s.title()
    
    for i in range(len(answer)):
        ch = answer[i]
        if ch.isdigit():
            answer = answer[:i+1] + answer[i+1].lower() + answer[i+2:]
    
    return answer