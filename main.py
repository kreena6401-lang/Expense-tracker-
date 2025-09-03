expenses = []

def add_expense(date, category, amount):
    expenses.append([date, category, amount])
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = 0
    print("--- Expense List ---")
    for date, category, amount in expenses:
        print(f"{date} | {category} | ₹{amount}")
        total += amount
    print(f"Total Expenses: ₹{total}")

def expense_tracker():
    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            try:
                amount = float(input("Enter amount: "))
                add_expense(date, category, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

expense_tracker()