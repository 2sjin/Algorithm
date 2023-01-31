def solution(quiz):
    OX = {True: "O", False: "X"}
    answer = [OX[eval(q.replace("=", "=="))] for q in quiz]
    return answer