"""
def solution(s):
    flag = 0
    for ch in s:
        # 여는 괄호면 +1, 닫는 괄호면 -1
        flag += 1 if ch == "(" else -1
        if flag < 0:         # 열기도 전에 닫으면 False
            return False
    
    # 여는 괄호와 닫는 괄호 쌍이 맞아야 True
    return True if flag == 0 else False
    a = 1
"""

# 스택 사용하기
from collections import deque

def solution(s):
    stack = deque()
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif len(stack) != 0:
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False