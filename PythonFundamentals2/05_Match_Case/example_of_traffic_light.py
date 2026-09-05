#alter native of if else
color =  input("Enter a color:")

match color:
    case "red":
        print("Stop")

    case "green":
        print("GO")

    case "yellow":
        print("Wait")

    case _:
        print("invalid input of colors")