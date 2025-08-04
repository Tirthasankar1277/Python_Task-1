
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == '5':
        print("Bye!")
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b == 0:
            print("Can't divide by zero.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid choice.")
