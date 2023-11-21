
gameList = ["Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa"]

# 1 - Iteration values of a list
for game in gameList:
    print(game)

# Continue and Break
# 2 - When the condition is met, the loop will complete

for game in gameList:
    if(game == "The Witcher"):
        break
    print(game)

# 3 - When the condition is met, the loop will go for the next iteration

for game in gameList:
    if(game == "The Witcher"):
        continue
    print(game)

# 4 - Classification of game
gameName = input("Type it the name of game: ")
gameRating = int(input("Type it how many classifications you wish make in game: "))

sum = 0
for i in range(gameRating):
    avaliation = float(input("What it is your avaliation for game?"))
    sum += avaliation

print(f"The Avarage of classification of game {gameName} is: {sum/gameRating}")