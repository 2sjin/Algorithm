"""
def solution(my_string, letter):
    str_list = list(my_string)
    while letter in str_list:
        str_list.remove(letter)
    answer = "".join(str_list)
    return answer
"""

def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer