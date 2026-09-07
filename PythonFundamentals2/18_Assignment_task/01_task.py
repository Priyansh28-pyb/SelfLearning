salary = int(input("Enter the salary : "))

if salary < 30000:
    print("Your tax rate on salary is : 5%")

elif salary > 30000 and salary < 70000 :
    print("Your tax rate on salary is : 15%")

elif salary > 70000 :
    print("Your tax rate on salary is : 25%")

else :
    print("Enter a valid value")