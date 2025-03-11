def solution(s):
    # isdigit : 숫자로만 이루어져 있는지 확인
    return s.isdigit() and (len(s) == 4 or len(s) == 6)