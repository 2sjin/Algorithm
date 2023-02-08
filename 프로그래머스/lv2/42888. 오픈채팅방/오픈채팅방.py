def solution(record):
    result = []
    nick = {}
    msg = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    
    for r in record:
        rec = r.split()
        if rec[0] in ("Enter", "Change"):
            nick[rec[1]] = rec[2]
            
    for r in record:
        rec = r.split()
        if rec[0] in ("Enter", "Leave"):
            result.append(nick[rec[1]] + "님이 " + msg[rec[0]])
            
    return result