def solution(myStr):
    sep = '|'
    answer = myStr.replace('a', sep).replace('b', sep).replace('c', sep)
    answer = [s for s in answer.split(sep) if not s == ""]
    return answer if answer else ["EMPTY"]