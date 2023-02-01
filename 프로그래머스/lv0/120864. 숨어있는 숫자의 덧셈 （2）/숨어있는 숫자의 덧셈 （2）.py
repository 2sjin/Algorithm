"""
from string import *

def solution(my_string):
    answer = ""
    for ch in my_string:
        answer += ch if not ch.isalpha() else " "
    try:
        return eval(answer.strip().replace("  ", " ").replace(" ", "+"))
    except:
        return 0
"""

# join과 sum 사용하기
def solution(my_string):
    result = ''.join(ch if ch.isdigit() else " " for ch in my_string)
    return sum(map(int, result.split()))