from expense import NewExpense

def main():
    print(f"Expense Tracker!")
    expenses =[]

    expense = get_user_expenses()
    expenses.append(expense)
    print(f"Saving the Expense: {expense['name']} in ({expense['cat']}) - Rs.{expense['amount']}")

    summrize(expenses)

    exit_menu()


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

def exit_menu():
    print("")

if __name__ == "__main__":
    main()