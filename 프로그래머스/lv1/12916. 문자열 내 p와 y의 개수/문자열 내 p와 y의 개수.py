"""
def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False
"""

def solution(s):
    return (lambda x: x.count('p') == x.count('y'))(s.lower())