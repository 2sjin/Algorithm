def solution(n, words):  
    for i, word in enumerate(words):
        # 앞사람의 마지막 문자로 이었는지 확인 
        if i > 0 and word[0] != words[i-1][-1]:
            return [i%n+1, i//n+1]
        # 중복 확인
        if word in words[:i]:
            return [i%n+1, i//n+1]
        
    return [0, 0]