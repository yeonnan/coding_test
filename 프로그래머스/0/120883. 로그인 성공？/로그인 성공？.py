def solution(id_pw, db):
    answer = 'fail'
    for i in db:
        if i == id_pw:
            return 'login'
        elif i[0] == id_pw[0]:
            return 'wrong pw'
    return answer