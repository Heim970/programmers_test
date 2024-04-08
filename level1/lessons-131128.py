# 코딩테스트 연습 > 연습문제 > 숫자 짝꿍
# 2024-04-08

def solution1(X, Y):     # 처음 제출한 코드
    X_o = {}
    for x in X:
        if x in X_o:
            X_o[x] += 1
        else:
            X_o[x] = 1

    match = []
    for y in Y:
        if y in X_o and X_o[y] > 0:
            match.append(y)
            X_o[y] -= 1

    if not match:
        match = "-1"
    elif match.count("0") == len(match):
        match = "0"
    else:
        match = ''.join(sorted(match, reverse=True))

    return match #

def solution(X, Y):   # 고친 코드
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * (min(X.count(str(i)), Y.count(str(i))))
    if not answer:
        answer = "-1"
    elif len(answer) == answer.count("0"):
        answer = "0"
    return answer

print(solution("100", "2345") == "-1")
print(solution("100", "203045") == "0")
print(solution("100", "123450") == "10")
print(solution("12321", "42531") == "321")
print(solution("5525", "1255") == "552")