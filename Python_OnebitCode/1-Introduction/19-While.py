gameName = input("Type it the name of game: ")
condition = 1;
sum = 0;
countAvaliations = 0;
while(condition != 0):
    avaliation = float(input("Type it a avaliation for game: "))
    sum += avaliation
    countAvaliations += 1
    condInput = int(input("You wish stop the avaliations?If yes type it '-1' "))
    condition = condInput

print(f"The Avarage of classification of game {gameName} is: {sum/countAvaliations}")