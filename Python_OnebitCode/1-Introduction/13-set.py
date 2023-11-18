gamesSet = {"Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa"}

# - Can't retrieve values by slice
# - Can't repeat value in set

print(gamesSet)

# 1 - Size of Set
print(len(gamesSet))

# 2 - True and number 1 are equals in the set
exampleSet = {"Silent Hill", "God of War 3", True, 1}
print(exampleSet)

# 3 - Add item of other set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remove a item in set
gamesSet.remove(True)
gamesSet.remove("Resident Evil 7")
print(gamesSet)