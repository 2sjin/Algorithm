def solution(numbers, direction):
    answer = numbers
    if direction == "right":
        answer.insert(0, answer.pop())
    else:
        answer.append(answer.pop(0))
    return answer