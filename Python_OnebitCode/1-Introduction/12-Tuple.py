gameTuple = ("Resident Evil 7", "Star Wars", "The Witcher", "Red Dead 2", "Fifa")
print(gameTuple)
print(type(gameTuple))

# - Can't add values in tuple
# - Can't remove values in tuple
# - Can't order values in tuple

# 1 - Search the two first items of tuple
print(gameTuple[:2])

# 2 - Search the last item of tuple
print(gameTuple[-1])

# 3 - Search games until a determines position
print(gameTuple[:3])

# 4 - Search games of a position in next
print(gameTuple[2:])

# 2 - Retrieve a item of tuple by index
print(gameTuple.index("The Witcher")) #Index 2

