def solution(my_string):
    answer = my_string
    for ch in 'aeiou':
        answer = answer.replace(ch, "")
    return answer