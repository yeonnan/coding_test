while True:
    n = list(map(int, input().split()))
    if n.count(0)==3:
        break
    n.sort()
    if n[2] ** 2 == n[0] ** 2 + n[1] ** 2:    # 피타고라스 성립하면
        print('right')
    else:
        print('wrong')