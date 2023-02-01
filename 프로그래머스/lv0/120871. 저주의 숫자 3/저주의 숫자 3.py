def solution(n):
    numbers = [i for i in range(186) if (i % 3 != 0) and ("3" not in str(i))]
    return numbers[n-1]
