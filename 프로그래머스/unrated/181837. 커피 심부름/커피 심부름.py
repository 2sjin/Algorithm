def solution(order):
    result = 0
    for x in order:
        result += 5000 if 'cafelatte' in x else 4500
    return result