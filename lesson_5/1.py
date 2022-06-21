# from pprint import pprint as print

LOGGING = True

team: list[dict] = [
    {"name": "John", "age": 20, "number": 12},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 14},
]


def repr_players(
    players: list[dict], sorted: bool = False, key: str = "number"
) -> None:
    print("TEAM:")
    if sorted:
        players.sort(key=lambda k: k[key])
    for player in players:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")
    print("\n")


def player_update(players: list[dict], num: int, name: str, age: int) -> None:
    check_number_flag = False
    for player in players:
        if player["number"] == num:
            check_number_flag = True
            player["age"] = age
            player["name"] = name
            break
    if not check_number_flag:
        log(message=f"Player with number {num} doesn't exist")


def log(message: str) -> None:
    print(f"**** {message} ****")


def add_player(team: list[dict], num: int, name: str, age: int) -> None:
    check_number_flag = False
    new_player = {"name": name, "number": num, "age": age}
    for player in team:
        if player["number"] == num:
            check_number_flag = True
            break
    if check_number_flag:
        log(message=f"Player with the number {num} is already exists.")
    else:
        team.append(new_player)
        log(message=f"Adding {new_player['name']}")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def main():
    repr_players(team)

    add_player(team, num=17, name="Cris", age=31)
    add_player(team, num=14, name="Bob", age=39)
    remove_player(players=team, num=14)
    player_update(team, num=16, name="Max", age=30)

    repr_players(team, sorted=True)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
