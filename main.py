from expense import NewExpense

def main():
    print(f"Expense Tracker!")
    expenses =[]

    summrize(expenses)

    while True:
        print("\nMain Menu")
        print("1. Add an expense")
        print("2. summrize expense")
        print("3. Exit")

        inp = input("Enter your choice [1 - 3]: ").strip()

        if inp == "1":
            expense = get_user_expenses()
            expenses.append(expense)
            print(f"Saving the Expense: {expense['name']} in ({expense['cat']}) - Rs.{expense['amount']}")
        elif inp == "2":
            summrize(expenses)
        elif inp == "3":
            exit_menu(expenses)
            break
        else:
            print("Invalid choice. Please try again!")


def get_user_expenses():
    print("Getting User Expenses")
    expense_name = input("Enter expense name: ")
    expense_ammount = float(input("Enter expense amount: "))

    categories = [
        "Food", 
        "Home", 
        "Work", 
        "Entertainment", 
        "Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(categories):
            print(f"{i+1}. {category_name}")

        category_index = int(input(f"Enter categrory number [1 - {len(categories)}]: ")) - 1

        if category_index in range(len(categories)):

            new_expense = NewExpense(name=expense_name, category=categories[category_index], amount=expense_ammount)
            return new_expense
        else:
            print("Invalid category. please try again!")

def summrize(expenses):
    amount_by_cat = {}
    for data in expenses:
        key = data['cat']
        if key in amount_by_cat:
            amount_by_cat[key] += data['amount']
        else:
            amount_by_cat[key] = data['amount']
    print("[] Expenses by category:")

    for key, amount in amount_by_cat.items():
        print(f" {key}: {amount}")

    total_spent = sum([x['amount'] for x in expenses])
    print(f"[] Total spent: {total_spent}")

def exit_menu(expenses):
    print(f"You recorded {len(expenses)} expenses on this run.")
    print("gg goodbye!")

if __name__ == "__main__":
    main()