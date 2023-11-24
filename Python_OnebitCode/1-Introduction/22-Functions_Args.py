# 1 - Function that receiver args

def full_name(firstName,lastName):
    print(f"{firstName} {lastName}")

full_name("Everson","Nascimento")

# 2 - Function sum

def sum(a,b):
   print(a+b) 

sum(2,5)

# 3 - Function with default value

def address(country = "Brasil"):
    print(f"I am from {country}")

address()
address("United States")