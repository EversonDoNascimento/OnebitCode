import pprint
games = {
    "Fifa": {
        "title": "Fifa 23",
        "yearLaunch": 2022,
        "gamePrice": 90,
        "classification": 9.6,
        "genre": ["Sport", "Family"]
    },
    "Mario Bross": {
        "title": "Mario Bross",
        "yearLaunch": 2000,
        "gamePrice": 56,
        "classification": 9.9,
        "genre": ["Adventure", "Family"]
    },
    "Resident Evil 7": {
        "title": "Resident Evil 7",
        "yearLaunch": 2016,
        "gamePrice": 150,
        "classification": 8.7,
        "genre": ["Horror", "Survivor"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games)

# 1 - Retrieve a element of dictionary
print(games['Resident Evil 7']['genre'])
print(games['Resident Evil 7'].get('genre'))

# 2 - Search itens of dictionary with key and value 
print(games["Fifa"].items())

# 3 - Add new item
games["Resident Evil 7"]["players"] = 1
pp.pprint(games["Resident Evil 7"])

# 4 - Remove a dictionary
del games["Fifa"]
pp.pprint(games)

title = input("name: ")
year = int(input("year: "))
game_name = input("name game: ")

games[game_name] = {"title": title, "year": year}
pp.pprint(games)
