def solution(arr):
    stack = []
    for i in arr:
        try:
            if stack[-1] != i:
                stack.append(i)
        except:
                stack.append(i)
    return stack