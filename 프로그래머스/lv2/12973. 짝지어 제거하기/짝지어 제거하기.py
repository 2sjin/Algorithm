def solution(s):
    stack = []
    
    for ch in s:
        if stack != [] and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
            
    return 1 if stack == [] else 0