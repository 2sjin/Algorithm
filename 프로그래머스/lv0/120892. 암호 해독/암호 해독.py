def solution(cipher, code):
    return "".join([x for x in cipher[code-1::code]])