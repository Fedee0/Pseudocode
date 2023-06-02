try:
    n = int(input("Enter the number of Fibonacci numbers you want to find: "))
    nmax = 20

    if n > 0:
        if not nmax <= n:
            f_1 = 1
            f_2 = 2
            f = 1

            k = 3
            while k < n:
                f = f_1 + f_2
                f_1 = f_2
                f_2 = f
                k = k + 1

            print(f"The {n}th Fibonacci number is {f}")

        else:
            print(f"Error: Please enter an integer less than {nmax}")
    else:
        print("Error: Please enter an integer greater than 0.")

except ValueError:
    print("Error: Please enter an integer")
