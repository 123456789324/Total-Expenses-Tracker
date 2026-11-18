import json
from datetime import datetime

# --------------------------------
# EXPENSE TRACKER
# --------------------------------

expenseslist = []

FILE_NAME = "expenses.json"


# 1. LOAD EXPENSES
def load_data():
    global expenseslist

    try:
        with open(FILE_NAME, "r") as file:
            expenseslist = json.load(file)

    except FileNotFoundError:
        expenseslist = []

    except json.JSONDecodeError:
        expenseslist = []

    print("Expense data loaded successfully.")


# 2. SAVE EXPENSES
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(expenseslist, file, indent=4)


# 3. ADD EXPENSE
def add_expense():

    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Try again.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenseslist.append(expense)
    save_data()

    print("Expense added successfully!")


# 4. VIEW ALL EXPENSES
def view_expenses():

    if len(expenseslist) == 0:
        print("No expenses found!")
        return

    print("\n========== ALL EXPENSES ==========")

    for count, each in enumerate(expenseslist, start=1):

        print(f"\nExpense No: {count}")
        print(f"Date: {each['date']}")
        print(f"Category: {each['category']}")
        print(f"Description: {each['description']}")
        print(f"Amount: Rs. {each['amount']}")


# 5. VIEW TOTAL EXPENSES
def total_expenses():

    total = 0

    for each in expenseslist:
        total += each["amount"]

    print(f"\nTotal Expenses = Rs. {total:.2f}")


# 6. EDIT EXPENSE
def edit_expense():

    view_expenses()

    if not expenseslist:
        return

    try:
        number = int(input("\nEnter expense number to edit: "))

        if number < 1 or number > len(expenseslist):
            print("Invalid expense number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = expenseslist[number - 1]

    print("Press Enter to keep the old value.")

    new_date = input("Enter new date: ")

    if new_date:
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            expense["date"] = new_date
        except ValueError:
            print("Invalid date. Old date kept.")

    new_category = input("Enter new category: ")
    if new_category:
        expense["category"] = new_category

    new_description = input("Enter new description: ")
    if new_description:
        expense["description"] = new_description

    new_amount = input("Enter new amount: ")

    if new_amount:
        try:
            amount = float(new_amount)

            if amount > 0:
                expense["amount"] = amount
            else:
                print("Invalid amount. Old amount kept.")

        except ValueError:
            print("Invalid amount. Old amount kept.")

    save_data()
    print("Expense updated successfully!")


# 7. DELETE EXPENSE
def delete_expense():

    view_expenses()

    if not expenseslist:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenseslist):
            print("Invalid expense number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        expenseslist.pop(number - 1)
        save_data()
        print("Expense deleted successfully!")

    else:
        print("Delete operation cancelled.")


# 8. SEARCH EXPENSE BY CATEGORY
def search_expense():

    category = input("Enter category to search: ").lower()

    found = False

    for count, each in enumerate(expenseslist, start=1):

        if each["category"].lower() == category:

            print(f"\nExpense No: {count}")
            print(f"Date: {each['date']}")
            print(f"Description: {each['description']}")
            print(f"Amount: Rs. {each['amount']}")

            found = True

    if not found:
        print("No expense found in this category.")


# 9. MONTHLY REPORT
def monthly_report():

    month = input("Enter month (YYYY-MM): ")

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format!")
        return

    total = 0

    print(f"\nReport for {month}")

    for each in expenseslist:

        if each["date"].startswith(month):

            print(
                each["date"],
                each["category"],
                each["amount"]
            )

            total += each["amount"]

    print(f"\nMonthly Total = Rs. {total:.2f}")


# 10. CATEGORY REPORT
def category_report():

    if not expenseslist:
        print("No expenses available.")
        return

    categories = {}

    for each in expenseslist:

        category = each["category"]

        if category in categories:
            categories[category] += each["amount"]

        else:
            categories[category] = each["amount"]

    print("\n====== CATEGORY REPORT ======")

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


# --------------------------------
# MAIN PROGRAM
# --------------------------------

load_data()

print("\nWelcome to Advanced Expense Tracker!")

while True:

    print("\n========== MAIN MENU ==========")

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Search Expense")
    print("7. Monthly Report")
    print("8. Category Report")
    print("9. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total_expenses()

    elif choice == 4:
        edit_expense()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        search_expense()

    elif choice == 7:
        monthly_report()

    elif choice == 8:
        category_report()

    elif choice == 9:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")