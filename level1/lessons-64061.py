# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# 2024-04-17

def solution(board, moves):
    basket = [0]
    answer = 0
    depth = [i for i in range(len(board))]
    for m in moves:
        for d in depth:
            if board[d][m-1] != 0:
                if basket[-1] == board[d][m-1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[d][m-1])
                board[d][m-1] = 0
                break
    return answer