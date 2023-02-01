def solution(n):
    answer = n
    for i in range(10):
        answer += 1
        if bin(n).count("1") == bin(answer).count("1"):
            break
        
    return answer
        