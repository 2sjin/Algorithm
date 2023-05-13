def solution(myString, pat):
    swap = myString.replace("A", "b").replace("B", "A").replace("b", "B")
    return 1 if pat in swap else 0