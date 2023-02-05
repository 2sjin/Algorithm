def solution(dartResult):
    score = []
    
    for i, ch in enumerate(dartResult):
        if ch.isdigit():
            if dartResult[i-1:i+1] == "10":
                score[-1] = 10
            else:
                score.append(int(ch))

        elif ch in "SDT":
            score[-1] **= "SDT".index(ch) + 1

        elif ch == "*":
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
        
        elif ch == "#":
            score[-1] *= -1
        
    return sum(score)