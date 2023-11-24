
'''
import winsound
x = 10
 
while x >= 0:
    print(x)
    x -= 1
   
winsound.Beep(2500,500)
'''
number = int(input("Type it multiplication table of: "))
begin = int(input("Of: "))
end = int(input("Until: "))

x = begin

while x <= end:
    print(f"Multiplication table of {number} x {x} = {number * x}")
    x += 1