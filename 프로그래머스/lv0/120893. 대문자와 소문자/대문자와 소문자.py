def solution(my_string):
    answer = ''
    for ch in my_string:
        answer += ch.lower() if ch.isupper() else ch.upper()
    return answer