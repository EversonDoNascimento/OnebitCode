letter = input("Type it a letter any: \n")
word = "fifa"
count = word.count(letter)

if count > 1:
    result = word[:1] + word[1:].replace(letter,"$")
    print(result)
else: 
    print("Not repeat")


word1 = input("Type it the first word: ")
word2 = input("Type it the second word: ")
print(f"{word1} {word2}")
resultfinal = word1.replace(word1[:2], word2[:2]) + " " + word2.replace(word2[:2], word1[:2])
print(resultfinal)

