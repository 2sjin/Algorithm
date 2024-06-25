def solution(my_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = []
    
    for x in alphabet:
        answer.append(my_string.count(x))
        
    return answer