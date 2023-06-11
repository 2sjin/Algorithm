def solution(myString):
    return "".join("l" if ch in "abcdefghijk" else ch for ch in myString)