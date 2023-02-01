def solution(emergency):
    emergency_sorted = sorted(emergency, reverse=True)
    return [emergency_sorted.index(x)+1 for x in emergency]