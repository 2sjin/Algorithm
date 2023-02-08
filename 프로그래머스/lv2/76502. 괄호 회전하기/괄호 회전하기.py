def check_correct(sub_str):
    stack = []
    for ch in sub_str:
        if ch in "({[":
            stack.append(ch)
        elif stack == [] or stack.pop() + ch not in ("()", "{}", "[]"):
            return False
    return True if stack == [] else False

def solution(s):
    result = 0
    for i in range(len(s)):
        if check_correct(s[i:] + s[:i]):
            result += 1
    return result