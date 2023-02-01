def solution(s, n):
    answer = ""
    
    for ch in s:
        # 공백은 그대로
        if ch == " ":
            answer += " "
            continue
    
        # 알파벳 대문자 여부 체크
        char_is_upper = ch.isupper()
    
        # 알파벳 암호화
        cipher_char = chr(ord(ch)+n)
        if char_is_upper and not cipher_char.isupper():
            cipher_char = chr(ord(ch)+n-26)
        elif not char_is_upper and not cipher_char.islower():
            cipher_char = chr(ord(ch)+n-26)

        answer += cipher_char
        
    return answer