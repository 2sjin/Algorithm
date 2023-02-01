from string import *

def solution(my_string):
    answer = ""
    for ch in my_string:
        answer += ch if not ch.isalpha() else " "
    try:
        return eval(answer.strip().replace("  ", " ").replace(" ", "+"))
    except:
        return 0