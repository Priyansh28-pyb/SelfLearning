


while True :
    n = int(input("Enter a number :"))
    if n > 0 :
        print(n ,"is a positive number")
    elif n < 0:
        print(n , "is a negative number")

    stop = input("Enter quit to stop this program : ")

    if stop == "quit" :
        break