def solution(sizes):
    answer = 0
    w_list = []
    h_list = []
    for i in sizes:
        i.sort()
        w_list.append(i[0])
        h_list.append(i[1])
    answer = max(w_list) * max(h_list)
    return answer