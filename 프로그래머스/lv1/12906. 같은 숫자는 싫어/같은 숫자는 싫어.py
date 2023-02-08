from collections import deque

def solution(arr):
    stack = deque()
    for i in arr:
        try:
            if stack[-1] != i:
                stack.append(i)
        except:
                stack.append(i)
    return tuple(stack)