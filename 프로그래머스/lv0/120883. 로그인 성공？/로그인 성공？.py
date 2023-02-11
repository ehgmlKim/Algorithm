def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        answer = "login"
    elif id_pw[0] in dict(db).keys():
        answer = "wrong pw"
    else:
        answer = "fail"
    return answer