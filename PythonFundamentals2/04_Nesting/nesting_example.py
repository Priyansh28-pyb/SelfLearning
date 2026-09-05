#nesting mae ek condition k andr jb dosri condition likh dete h tb nesting ati h
username = input("Enter user name :")
password = input("Enter password :")

if (username == "admin" and password == "pass"):
    print("succesfully login")

else:
    if(username != "admin"):
        print("username is wrong")
    else:
        print("password is wrong")