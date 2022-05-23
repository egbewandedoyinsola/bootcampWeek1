print("This program is a simple CLI calculator that can perform: addition, subtraction, division, multiplication and modulus operations")
while True:

    print("Enter 1 if you want division")
    print("Enter 2 if you want multiplication")
    print("Enter 3 if you want addition")
    print("Enter 4 if you want subtraction")
    print("Enter 5 if you want modulus operation")
    print("Enter Q or q to quit")

    selection = input(
        "Kindly enter the integer number of the operation you would like to perform : ")

    if selection == "Q" or selection == "q":
        print()
        break

    num1 = float(input("Enter your first number : "))
    num2 = float(input("Enter your second number : "))

    if selection == "1":
        if num2 == 0.0:
            print("Error : you can't divide by zero")
        else:
            print(num1, "/", num2, "=", (num1/num2))

    elif selection == "2":
        print(num1, "*", num2, "=", (num1*num2))

    elif selection == "3":
        print(num1, "+", num2, "=", (num1+num2))

    elif selection == "4":
        print(num1, "-", num2, "=", (num1-num2))

    elif selection == "5":
        if num2 == 0.0:
            print("Error : you can't divide by zero")
        else:
            print(num1, "%", num2, "=", (num1 % num2))

    else:
        print("wrong selection")

    print()
