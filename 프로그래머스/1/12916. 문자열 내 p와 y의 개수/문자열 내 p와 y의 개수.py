def solution(s):
    a = s.lower()
    if a.count('p') == a.count('y'):
        return True
    else:
        return False
        