def lowerOrUpper(word):
    countUpper = 0
    countLower = 0
    print(word)
    for w in word:
        if(w == " "):
            continue
        elif(word.upper().find(w) > -1):
            countUpper += 1
        else:
            countLower += 1

    print(f"This word contains {countLower} lowercase letters  and {countUpper} uppercase")


lowerOrUpper("everson")

def verify_char(text):
    type = {"Lowercase": 0, "Uppercase": 0}
    for char in text:
        if char.islower():
            type["Lowercase"] += 1
        elif char.isupper():
            type["Uppercase"] += 1
    print(f"Your original word is: {text}")
    print(f"This word contains {type['Lowercase']} lowercase letters")
    print(f"This word contains {type['Uppercase']} uppercase letters")

verify_char("Everson NAscimento")

def evenOrOdd(*numbers):
    listEven = []
    listOdd = []
    for num in numbers:
        even = lambda num: num%2 == 0
        if(even(num)):
            listEven.append(num)
        else:
            listOdd.append(num)
    print(f"Your Even list  is: {listEven} and your Odd list  is: {listOdd}")

evenOrOdd(2,3,5,2,4,5,6,7,4,5,7)

