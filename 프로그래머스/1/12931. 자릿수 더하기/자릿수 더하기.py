def solution(n):
    answer = 0
    for i in str(n):    # 각 자릿수를 분리하기 위해 문자열로 변환 
        answer += int(i)
    return answer