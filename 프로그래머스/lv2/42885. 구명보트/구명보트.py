from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    
    while len(deq) > 0:
        if len(deq) >= 2 and deq[0] + deq[-1] <= limit:
            deq.popleft()
        deq.pop()
        answer += 1
    
    return answer