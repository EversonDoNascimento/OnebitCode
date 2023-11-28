gameFifa = ["Fifa 23", 2022, 90.3, True]
print(gameFifa)

gameList = ["Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa"]

print(gameList)

# 1 - Search the first two items of list
print(gameList[:2])

# 2 - Search the last item of list
print(gameList[-1])

# 3 - Search games until a determines position
print(gameList[:3])

# 4 - Search games of a position in next
print(gameList[1:4])

list = ["Everton", "Everson"]


for i, item in enumerate(list):
    print(f"{i} {item}")