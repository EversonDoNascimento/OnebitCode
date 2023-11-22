gameList = ["Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa"]

# Use list Comprehension 
newList = [game for game in gameList if "a" in game]
print(newList)

# Without list Comprehension
newListNoComprehension = []
for game in gameList:
    if "a" in game:
        newListNoComprehension.append(game)
print(newListNoComprehension)

ListNumbersEven = [i for i in range(20) if (i%2) == 0] 
print(ListNumbersEven)