# Function Factorial

# 4 x 3 x 2 x 1 = 24
def factorial(num):
    if(num == 1):
        return 1
    else:
       return num * factorial(num - 1)

'''
init = 4
4 == 1? false

4 * {factorial(3)= 6} = 24
3 == 1? 

3 * {factorial(2)= 2}
2 == 1? false

2 * factorial(1)
1 == 1? true
break
6 * 4 = 24


'''


print(factorial(5))

#Sum

def sum(num):
    if(num == 1):
        return 1
    else:
        print(num + sum(num - 1))
        return num + sum(num - 1)

# 4 + sum(4 - 1) = 10
# 3 + sum(3 - 1) = 6
# 2 + sum(2 - 1) = 3
# return 1 

print(sum(4))