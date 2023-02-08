def solution(record):
    result = []
    nick = {}
    
    for r in record:
        rec = r.split()
        if rec[0] in ("Enter", "Change"):
            nick[rec[1]] = rec[2]
            
    for r in record:
        rec = r.split()
        if rec[0] == "Enter":
            result.append(nick[rec[1]] + "님이 들어왔습니다.")
        elif rec[0] == "Leave":
            result.append(nick[rec[1]] + "님이 나갔습니다.")
            
    return result