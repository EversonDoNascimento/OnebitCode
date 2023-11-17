gameDescription = '''
    Fifa é unm jogo de futebol,
    desenvolvido pela EA sports
'''
gameName = "Fifa 23"

print(gameName.upper())#Return string Uppercase
print(gameName.lower())# Return string LowerCase
print(gameName.capitalize())# The first letter in Uppercase
print(gameName.title())# The first letter in Uppercase
print(gameName.center(20, '-')) # Return the string in center with the fill of character
print(gameName.find("a")) # Return the position of a determines character
print(gameName.count("f")) # Count characters
print(gameName.replace("Fifa","Pes"))
print(gameDescription.split(','))