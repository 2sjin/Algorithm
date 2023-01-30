def solution(numbers):
    answer = numbers
    num_alpha = ("zero", "one", "two", "three", "four",
                 "five", "six", "seven", "eight", "nine")
    
    for a in num_alpha:
        answer = answer.replace(a, str(num_alpha.index(a)))
    
    return int(answer)