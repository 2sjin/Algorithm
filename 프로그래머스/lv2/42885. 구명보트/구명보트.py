from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    
    while True:
        length = len(deq)
        if length <= 0:
            break
        if length >= 2 and deq[0] + deq[-1] <= limit:
            deq.popleft()
        deq.pop()
        answer += 1
    
    return answer