def solution(ingredient):
    answer = 0
    n = []
    for i in ingredient:
        n.append(i)
        if n[-4:] == [1, 2, 3, 1]:
            answer += 1
            for k in  range(4):
                n.pop()
    return answer