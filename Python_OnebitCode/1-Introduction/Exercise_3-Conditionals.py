'''

* Calculate of distance

-> Write a program that ask the distance that passengers wish traverse in km. 
   Calculate the price of ticket, R$ 0.50 by of charging km for travel of until 
   200 km, and R$ 0.35 for more long travel.

* Salary increase

-> Write a program that ask the salary of employee and calculate the value of increase
   For Salaries above R$ 1.250,00, calculate a increase of 10% for the belows or iquals,
   of 15%


'''

travelDistance = float(input("Type it the distance of your travel: \n"))

if(travelDistance <= 200):
    print(f"Your ticket cost: R$ {travelDistance*0.50:.2f}")
else:
    print(f"Your ticket cost: R$ {travelDistance*0.35:.2f}")

increaseSalary = float(input("Type it the value of your salary: \n"))

if(increaseSalary >= 1250):
    print(f"Your new salary is: {increaseSalary + (increaseSalary*0.10)}")
else:
    print(f"Your new salary is: {increaseSalary + (increaseSalary*0.15)}")