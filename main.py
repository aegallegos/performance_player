import charts
import read_csv
import utils


def run():
    data = read_csv.read_csv(
        "./performance_player/fifa_world_cup_2026_player_performance.csv"
    )
    try:
        goals = int(input("Ingrese el numero de goles: "))
        if goals > 0:
            players = utils.goals_by_player(data, goals)
            if len(players) > 0:
                labels, values = utils.get_players(players)
                charts.generate_bar_chart(labels, values)
                charts.generate_pie_chart(labels, values)
        else:
            raise Exception("Numero debe ser mayor que 0")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run()
