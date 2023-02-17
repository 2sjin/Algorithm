from collections import deque

def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    
    for word in goal:
        if len(queue1) > 0 and word == queue1[0]:
            queue1.popleft()
        elif len(queue2) > 0 and word == queue2[0]:
            queue2.popleft()
        else:
            return "No"

    return "Yes"