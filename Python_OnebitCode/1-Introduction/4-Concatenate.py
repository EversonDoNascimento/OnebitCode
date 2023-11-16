name = input("Type it the name of game:\n")
yearLaunch = int(input("Type it the release year of game:\n "))
gamePrice = float(input("Type it the price of Game:\n"))
planInclude = input("Is included in the monthly service?\n ")

# Alternative 1
'''
print("The Name of Game is: " + name)
print("The Year of Game is: " , yearLaunch)
print("The Price of Game is: " , gamePrice)
print("The Status Plan of Game is: ", planInclude)
'''
# Alternative 2
'''
print("The Name of Game is: ", name, "\n The Year of Game is:", yearLaunch,
      "\n The Price of Game is:", gamePrice, "\n The Status Plan of Game is: ", planInclude)
'''

# Alternative 3


print(f"The Name of Game is: {name} \nThe Year of Game is: {yearLaunch} \nThe price of game is: {gamePrice} \nThe status Plan of Game is: {planInclude}")
