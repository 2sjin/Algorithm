def solution(babbling):
    answer = 0
    
    for bab in babbling:
        checking_str = bab
        for word in ("aya", "ye", "woo", "ma"):
            checking_str = checking_str.replace(word, " ")
        if checking_str.strip() == "":
            answer += 1
        
    return answer