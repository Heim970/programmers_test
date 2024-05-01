# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
# 2024-05-01

pads = {1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        10: (3, 0), 0: (3, 1), 12: (3, 2)}


def distance(n, fl, fr):
    li, lj = pads[fl]
    ri, rj = pads[fr]
    ni, nj = pads[n]

    dl = abs(li - ni) + abs(lj - nj)
    dr = abs(ri - ni) + abs(rj - nj)

    return dl, dr


def solution(numbers, hand):
    answer = ''
    fl = 10
    fr = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            fl = i
        elif i in [3, 6, 9]:
            answer += 'R'
            fr = i
        else:
            dl, dr = distance(i, fl, fr)
            if dl < dr:
                answer += 'L'
                fl = i
            elif dl > dr:
                answer += 'R'
                fr = i
            elif dl == dr:
                if hand == 'left':
                    answer += 'L'
                    fl = i
                else:
                    answer += 'R'
                    fr = i
    return answer