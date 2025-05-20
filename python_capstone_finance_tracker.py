def add_expense(data):
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")
        
        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount < 0:
            raise ValueError("Amount must be positive.")

        expense = (description, amount)

        if category in data:
            data[category].append(expense)
        else:
            data[category] = [expense]

        print("Expense added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_expenses(data):
    if not data:
        print("No expenses to display.")
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    if not data:
        print("No expenses to summarize.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    print("Welcome to the Personal Finance Tracker!")
    expenses_data = {}

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses_data)
        elif choice == "2":
            view_expenses(expenses_data)
        elif choice == "3":
            view_summary(expenses_data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
