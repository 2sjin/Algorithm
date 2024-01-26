def solution(my_string, s, e):
    result = ""
    for i in range(s):
        result += my_string[i]
    for i in range(e, s-1, -1):
        result += my_string[i]
    for i in range(e+1, len(my_string)):
        result += my_string[i]
    return result