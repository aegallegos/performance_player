"""
El presente codigo procesa del archivo csv el cual contiene el desempeño de varios jugadores
de las eliminatorias del mundial 2026, entre los cuales estan el # de goles anotados. Se muestra
un grafico de barras y de pastel de los jugadores que han anotado goles de acuerdo a la cantidad
ingresada por el usuario.
Curso Platzi
"""

import charts
import read_csv
import utils


def run():
    # Lee el archivo csv, a traves de la funcion read_csv
    data = read_csv.read_csv(
        "./performance_player/fifa_world_cup_2026_player_performance.csv"
    )
    try:
        # Se solicita al usuario ingresar el numero de goles
        goals = int(input("Ingrese el numero de goles: "))
        # Valida que se ingresa una cantidad mayor que 0
        if goals > 0:
            players = utils.goals_by_player(data, goals)
            # Valida que la lista contenga al menos un jugador
            if len(players) > 0:
                labels, values = utils.get_players(players)
                charts.generate_bar_chart(labels, values)
                charts.generate_pie_chart(labels, values)
            else:
                print("No se econtraron Jugadores con la cantidad de goles ingresados")
        else:
            raise Exception("Numero debe ser mayor que 0")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run()
