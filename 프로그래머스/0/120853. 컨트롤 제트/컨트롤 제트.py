def solution(s):
    arr = s.split(' ')
    answer =[]
    
    for i in arr :
        if i == 'Z':
            answer.pop()
        else:
            answer.append(int(i))
            
    return sum(answer)