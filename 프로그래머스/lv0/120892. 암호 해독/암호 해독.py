def solution(cipher, code):
    answer = "".join([x for x in cipher[code-1::code]])
    return answer