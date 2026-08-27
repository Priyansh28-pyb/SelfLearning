age = int(input("Enter your age : "))

if age < 13 and age > 0:
    print("You are child")

elif age > 13 and age < 18 :
    print("You are teenager")

elif age >= 18 and age < 100 :
    print("You are adult ")

else:
    print("Enter a valid age")