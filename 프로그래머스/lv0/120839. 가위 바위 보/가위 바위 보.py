def solution(rsp):
    answer = rsp
    answer = answer.replace("0", "p").replace("2", "r").replace("5", "s")
    answer = answer.replace("r", "0").replace("s", "2").replace("p", "5")
    return answer