history = []

while True:
    print("\n========== CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Exit")

    try:
        choice = int(input("Choose Your Choice Number Please: "))

        if choice == 1:
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))

            result = a + b
            print("Answer:", result)
            history.append(f"{a} + {b} = {result}")

        elif choice == 2:
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))

            result = a - b
            print("Answer:", result)
            history.append(f"{a} - {b} = {result}")

        elif choice == 3:
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))

            result = a * b
            print("Answer:", result)
            history.append(f"{a} * {b} = {result}")

        elif choice == 4:
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))

            if b == 0:
                print(" Cannot divide by zero.")
            else:
                result = a / b
                print("Answer:", result)
                history.append(f"{a} / {b} = {result}")

        elif choice == 5:
            if len(history) == 0:
                print(" No history available.")
            else:
                print("\n===== HISTORY =====")
                for item in history:
                    print(item)

        elif choice == 6:
            print(" Thank you for using the calculator!")
            break

        else:
            print("Please choose a number between 1 and 6.")

    except ValueError:
        print(" Invalid input! Please enter only numbers.")