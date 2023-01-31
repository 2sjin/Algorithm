"""
def solution(numbers, direction):
    answer = numbers
    if direction == "right":
        answer.insert(0, answer.pop())
    else:
        answer.append(answer.pop(0))
    return answer
"""

# 리스트 슬라이싱 활용
def solution(numbers, direction):
    answer = numbers
    if direction == "right":
        answer = answer[-1:] + answer[:-1]
    else:
        answer = answer[1:] + answer[:1]
    return answer