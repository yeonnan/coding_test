def solution(t, p):
    answer = 0
    p_len = len(p)      # p의 길이 계산
    
    for i in range(len(t) - p_len + 1):
        substring = t[i:i + p_len]       
        if int(substring) <= int(p):       
            answer += 1
    return answer