team: list[dict] = [
    {"name": "John", "age": 20, "number": 12},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 14},
]


def repr_players(
    players: list[dict], sorted: bool = False, key: str = "number"
) -> None:
    print("TEAM:")
    # sorted(players, key=lambda k: k['number'])
    players.sort(key=lambda k: k["number"])
    for player in players:
        print(player["number"])
    for player in players:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")
    print("\n")


repr_players(team)
