def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Highest Expense")
    print("6. Exit")

expenses = []

def add_expense(amount_received, category_received):
    expenses.append({"amount": amount_received, "category": category_received})
    print("Expense added successfully!")

def view_expense():
    digit = 1
    print("All Expenses:")
    for item in expenses:
        print(f"{digit}. {item["amount"]} - {item["category"]}")
        digit +=1

def total_spending():
    total_spent = 0
    for spending in expenses:
        total_spent += spending["amount"]
    print(f"Total Spending: {total_spent} PKR")


# def category_summary():
#     print("Category-wise Spending: ")
#     summary = {}
#     for item in expenses:
#         category1 = item["category"]
#         amount1 = item["amount"]
#
#         if category1 in summary:
#             summary[category] += amount
#         else:
#             summary[category] =amount
#     for cat, amt in summary.items():
#         print(f"{cat}: {amt} PKR")


def highest_expense():
    print("Highest Expense: ")

    highest_expense = 0
    highest_category = ""
    for highest in expenses:
        if highest["amount"] > highest_expense:
            highest_expense = highest["amount"]
            highest_category = highest["category"]
        else:
            pass
    print(f"Amount: {highest_expense} PKR")
    print(f"Category: {highest_category}")



is_on = True

while is_on:
    menu()
    user_choice =int(input("Enter the operation you want to perform. "))

    if user_choice == 1:
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)

    elif user_choice == 2:
        view_expense()
    elif user_choice == 3:
        total_spending()
        pass
    # elif user_choice == 4:
    #     category_summary()
    #     pass
    elif user_choice == 5:
        highest_expense()
        pass
    elif user_choice == 6:
        print("Exiting program... Goodbye!")
        is_on = False
