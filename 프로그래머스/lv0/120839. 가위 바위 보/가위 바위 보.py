"""
def solution(rsp):
    answer = rsp.replace("0", "p").replace("2", "r").replace("5", "s")
    answer = answer.replace("r", "0").replace("s", "2").replace("p", "5")
    return answer
"""

# 딕셔너리 사용
def solution(rsp):
    dic = {"0":"5", "2":"0", "5":"2"}    
    return "".join(dic[x] for x in rsp)