# 코딩테스트 연습 > 연습문제 > 대충 만든 자판
# 2024-03-31 ChatGPT 코드(일부수정)

def solution(keymap, targets):
    dic = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in dic or i + 1 < dic[key]:
                dic[key] = i + 1
    
    answer = []
    for word in targets:
        result = 0
        for char in word:
            if char not in dic:
                result = -1
                break
            result += dic[char]
        answer.append(result)

    return answer