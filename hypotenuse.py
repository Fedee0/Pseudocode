try:
    c_1 = int(input("Enter the value of the first cathetus: "))
    c_2 = int(input("Enter the value of the second cathetus: "))

    if c_1 > 0 and c_2 > 0:
        h = (c_1 ** 2 + c_2 ** 2) ** (1 / 2)
        print(f"The hypotenuse of the catheters {c_1} and {c_2} is {round(h)}")

    else:
        print("Both catheters must have a value other than 0")

except ValueError:
    print("Invalid input. Please enter an integer")
