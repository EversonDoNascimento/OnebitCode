name = input("type it the name of game:")
yearLaunch = int(input("Type it the year release of game:"))
classification = float(input("Type it the note of classification of game:"))

if classification > 8.0:
    print(f"The game {name} is good!")
else:
    print("The game {name}, maybe not is good!")