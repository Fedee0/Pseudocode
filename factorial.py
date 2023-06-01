try:
    n = int(input("The number whose factorial you want to find: "))
    if n > 0:
        k = 1
        f = 1

        while n > k:
            f = f * (k + 1)
            k = k + 1

        print(f"Factorial of {n} is {f}")

    else:
        print("Invalid input. Please enter a positive integer.")

except ValueError as e:
    print("Invalid input. Please enter an integer")
