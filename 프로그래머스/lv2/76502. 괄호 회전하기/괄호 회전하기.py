from collections import deque

def check_correct(sub_str):
    stack = deque()
    for ch in sub_str:
        if ch in "({[":
            stack.append(ch)
        elif len(stack) == 0 or stack.pop() + ch not in ("()", "{}", "[]"):
            return False
    return True if len(stack) == 0 else False

def solution(s):
    result = 0
    for i in range(len(s)):
        if check_correct(s[i:] + s[:i]):
            result += 1
    return result