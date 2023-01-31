def solution(my_str, n):
    answer = [my_str[n*i:n*i+n] for i in range((len(my_str)//n) + 1)]
    if "" in answer:
        answer.remove("") 
    return answer