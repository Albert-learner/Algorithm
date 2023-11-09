# Restart 36. 달리기 경주

def solution(players, callings):
    answer = players

    players_ranking = {player : int(player_rank) for player_rank, player in enumerate(players)}

    for call_player in callings:
        passing_player_rank = players_ranking[call_player]
        players_ranking[call_player] -= 1
        players_ranking[answer[passing_player_rank - 1]] += 1

        answer[passing_player_rank - 1], answer[passing_player_rank] = call_player, answer[passing_player_rank - 1]
    return answer

players_1 = ['mumu', 'soe', 'poe', 'kai', 'mine']

callings_1 = ['kai', 'kai', 'mine', 'mine']

print(solution(players_1, callings_1))