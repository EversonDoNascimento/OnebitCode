gameFifa = {
  "title": "Fifa 23",
  "yearLaunch": 2022,
  "gamePrice": 90,
  "classification": 9.6,
  "genre": ["Sport", "Family"]

 }

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Retrieve a element of dictionary
print(gameFifa['title'])
print(gameFifa.get('genre'))

# 2 - Search just the keys of dictionary
print(gameFifa.keys())

# 3 - Search just the values of dictionary
print(gameFifa.values())

# 4 - Search itens of dictionary with key and value 
print(gameFifa.items())

# 5 - add items in dictionary
gameFifa["players"] = 2
print(gameFifa)

# 6 - Update items in dictionary
gameFifa.update({'players': 1})
print(gameFifa)

# 7 - Remove item of dictionary
gameFifa.pop("players")
print(gameFifa)
