gameList = ["Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa"]

# 1 - Size of list
print(len(gameList))

# 2 - Retrieve a item of list by index
print(gameList.index("The Witcher")) #Index 2

# 3 - Add item in end of list

gameList.append("God Of War 4")
print(gameList)

# 4 - Order the list
gameList.sort()
print(gameList)

# 5 - copy the items of a list for other list
gameReset = gameList.copy()
gameReset.remove("The Witcher")
print(gameReset)

#6 - Delete all items of list
gameList.clear()
print(gameList)