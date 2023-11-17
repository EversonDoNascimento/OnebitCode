gameDescription = '''
    Fifa é unm jogo de futebol
    desenvolvido pela EA sports
'''
gameName = "Fifa 23"

#string[init:end] - index beging in position 0 | end index -1

# 1 - Search all string beginging of first position
print(gameName[0:])

# 2 - Search all string  until the last position
print(gameName[:7])

# 3 - Search all string of third until the last position

print(gameName[2:])
'''

string[init:end] - index beging in position 0 | end index -1
step - determines the increment. By default this number is 1.

'''

# 4 - Search all string of 2 in 2 chacteres
print(gameName[::2])

# 5 - Search all string in odd index
print(gameName[1::2])

# 6 - reverse a string backwards

print(gameName[::-1])