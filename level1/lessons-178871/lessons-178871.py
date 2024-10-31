# 코딩테스트 연습 > 연습문제 > 달리기 경주
# 2024-10-31
# with ChatGPT

def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    players_list = players[:]

    for name in callings:
        current_rank = rank[name]
        front = players_list[current_rank - 1]
        players_list[current_rank - 1], players_list[current_rank] = name, front

        rank[name] = current_rank - 1
        rank[front] = current_rank

    return players_list
