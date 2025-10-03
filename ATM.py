def atm():
    pin = "4248"
    balance = 1000  # starting balance

    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Ask for PIN before every operation
        if choice in ["1", "2", "3"]:
            entered_pin = input("Enter PIN to continue: ")
            if entered_pin != pin:
                print("Wrong PIN! Access denied.\n")
                continue  # back to menu

        if choice == "1":   # Check Balance
            print("Your balance is: $4", balance)

        elif choice == "2":   # Withdraw
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance: ₹", balance)

        elif choice == "3":   # Deposit
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("₹", amount, "deposited successfully.")
            print("Updated balance: ₹", balance)

        elif choice == "4":   # Exit
            print("Thank you for using this ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

atm()