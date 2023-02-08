from collections import deque

def solution(priorities, location):
    queue = deque([f"{i}:{prio}" for i, prio in enumerate(priorities)])
    printed = deque()
    
    while queue:
        front = queue.popleft()
        if queue and front[-1] < max(i[-1] for i in queue):
            queue.append(front)
        else:
            printed.append(front)
    
    return [printed.index(x)+1 for x in printed if int(x[:-2]) == location][0]