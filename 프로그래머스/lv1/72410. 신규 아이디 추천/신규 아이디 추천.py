def solution(new_id):
    # 1단계
    result = new_id.lower()
    
    # 2단계
    result = "".join([ch for ch in result if ch.islower() or ch.isdigit() or ch in "-_."])
    
    # 3단계
    while ".." in result:
        result = result.replace("..", ".")

    # 4단계
    if result in (".", ".."):
        result = ""
    else:
        if result[0] == ".":
            result = result[1:]
        if result[-1] == ".":
            result = result[:-1]
    
    # 5단계
    if result == "":
        result = "a"
    
    # 6단계
    if len(result) >= 16:
        result = result[:15]
    if result[-1] == ".":
        result = result[:-1]
    
    # 7단계
    while len(result) <= 2:
        result += result[-1]
    
    # 결과 반환
    return result