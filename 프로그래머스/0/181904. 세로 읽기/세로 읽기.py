def solution(my_string, m, c):
    return my_string[c-1::m]
    
"""
def solution(my_string, m, c):
    result = ""
    cursor = 0
    for i in range(len(my_string)//m):
        s = my_string[cursor:cursor+m]
        result += s[c-1]
        cursor += m
    return result
"""