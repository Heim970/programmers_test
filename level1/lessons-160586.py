# 코딩테스트 연습 > 연습문제 > 대충 만든 자판
# 2024-03-31

def solution(keymap, targets):
    dic = {}
    for keys in keymap:
        for key in keys:
            if key in dic:
                if keys.index(key) + 1 < dic[key]:
                    dic[key] = keys.index(key) + 1
            else:
                 dic[key] = keys.index(key) +1
    
    answer = []
    for word in targets:
        result = 0
        for i in word:
            if i not in dic:
                result = -1
                break
            else:
                result += dic[i]
        answer.append(result)

    return answer