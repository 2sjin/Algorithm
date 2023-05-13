def solution(n, control):
    dic = {"w":"+1", "s":"-1", "d":"+10", "a":"-10"}
    return n + eval("".join(dic[x] for x in control))
    
    """
    control = control.replace("w", "+1")
    control = control.replace("s", "-1")
    control = control.replace("d", "+10")
    control = control.replace("a", "-10")
    return eval(str(n) + control)
    """