# from pprint import pprint as print


team = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kevin", "age": 17, "number": 12},
]


def repr_players(players: list([dict])) -> None:
    print("TEAM:")
    for player in players:
        print(f"\t{player['number']} Name: {player['name']}, Age: {player['age']}")
    print("\n")


def add_player(number: int, name: str, age: int) -> None:
    player = {"name": name, "number": number, "age": age}
    team.append(player)


def remove_payer(players: list[dict], number: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == number:
            # player_name = player["name"]
            del player[index]


def main():
    add_player(number=17, name="Cris", age=31)
    add_player(number=18, name="Bob", age=39)
    repr_players(team)


if __name__ == "__main__":
    main()
else:
    print("This module can not be imported")
