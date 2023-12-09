'''
a = append
r = read
w = write

'''
# 1 

"""file = open('data/names.txt','a',encoding = 'utf-8')
name = input("Type it a name: ")
file.write(f"{name}\n")
file.close"""

# 2

name = input("Type it a name: ")
with open("data/names.txt",'a',encoding='utf-8') as file:
    file.write(f"{name}\n")
