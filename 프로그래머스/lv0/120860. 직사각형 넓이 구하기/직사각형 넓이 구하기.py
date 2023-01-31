def solution(dots):
    width = (lambda x: max(x) - min(x))([d[0] for d in dots])
    height = (lambda y: max(y) - min(y))([d[1] for d in dots])
    return width * height