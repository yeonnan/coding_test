def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i%divisor == 0:      # divisor로 나누어 떨어지는 값만 answer에 추가
            answer.append(i)
            
    if len(answer) == 0:        # 나누어 떨어지는 값이 없으면 -1 추가
        answer.append(-1)
    answer.sort()
    return answer