num1 = int(input("Enter the num from start with : "))
num2 = int(input("Enter the num from end with :"))

def even(num1 , num2):
    for i in range(num1 , num2+1 ):
        if i  % 2 == 0:
            print(i)

even(num1 , num2)