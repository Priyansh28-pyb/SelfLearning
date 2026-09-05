print("Welcome to Admin Panel ")
username = input("Enter your username :")
password = input("Enter your password :")

if username == "admin" and password == "pass" :
    print("You are admin , succesfully logged in")

elif username != "admin" :
    print("User doesnt exist")

else:
    print("password is incorrect")