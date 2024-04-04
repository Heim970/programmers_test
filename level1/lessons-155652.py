# 코딩테스트 연습 > 연습문제 > 둘만의 암호
# 2024-04-04

def solution(s, skip, index):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        alphabet.remove(i)
    answer = ''
    for st in s:
        answer += alphabet[(alphabet.index(st)+index)%(len(alphabet))]
    return answer