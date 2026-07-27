def get_players(players_dic):
    players_goals_dic = {
        player["player_name"]: int(player["goals"]) for player in players_dic
    }
    labels = players_goals_dic.keys()
    values = players_goals_dic.values()
    return labels, values


def goals_by_player(data, goals):
    result = list(
        filter(lambda item: int(item["goals"]) >= goals, data)
    )  # retorna lista de jugadores que han marcado mas goles que el número ingresado por el usuario
    return result
