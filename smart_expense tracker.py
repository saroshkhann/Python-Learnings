from datetime import datetime
import requests
import smtplib

class ExpenseTracker:
    def __init__(self):
        self.users= {}
        self.MY_EMAIL = "ksarosh137@gmail.com"
        self.MY_PASSWORD = "uhjqjsimetltfurm"

    def get_username(self):
        username = input("Enter username: ")
        return username

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists")

            self.users[username]= {
                "expenses": [],
                "budget": 0
            }

            print(f"User '{username}' registered successfully!")

        except ValueError as e:
            print(f"Error: {e}")

    def monthly_budget(self, username, m_budget):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            user["budget"] = m_budget


            print("Budget set successfully!")
            print(f"User: {username}")
            print(f"Budget: {m_budget}")

        except ValueError as e:
            print(f"Error: {e}")

    def add_expense(self, username, category, amount):
        try:
            if username not in self.users:
                raise ValueError("User does not exists!")

            user = self.users[username]
            date = datetime.now().date()

            user["expenses"].append({"category": category, "amount": amount, "date":f"{date}"})
            print("Expense added successfully!")


        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            print("-------- EXPENSE LIST --------")
            print(f"User: {username}")

            user = self.users[username]
            expenses = user["expenses"]

            if len(expenses) == 0:
                print("No expenses found for this user!")
                return

            counter = 1
            for expense in expenses:
                print(f"{counter}. {expense['category']} | {expense['amount']} PKR | {expense['date']}")
                counter+=1
            print("-----------------------------")
            print(f"Total Entries: {len(expenses)}")
        except ValueError as e:
            print(f"Error: {e}")

    def expense_analytics(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            print("-------- EXPENSE ANALYTICS --------")
            print(f"User: {username}")

            # EXPENSE
            total_expense = 0
            user = self.users[username]
            expenses = user["expenses"]

            if len(expenses) == 0:
                print("No expenses to analyze")
                return

            for expense in expenses:
                total_expense += expense["amount"]
            print(f"Total spending: {total_expense} PKR")

            # BUDGET
            budget = user["budget"]
            if budget == 0:
                print("Budget not set!")
                return

            print(f"Budget: {budget} PKR")

            # REMAINING BUDGET
            remaining_budget = budget - total_expense
            print(f"Remaining Budget: {remaining_budget} PKR")

            # CATEGORY BREAKDOWN
            print("Category Breakdown")
            for expense in expenses:
                print(f"- {expense['category']} : {expense['amount']} PKR")

            # MAXIMUM AMOUNT
            print("Most Spent Category: ")

            most_expense = 0
            most_category = ""

            for item in expenses:
                if item["amount"] > most_expense:
                    most_expense = item["amount"]
                    most_category = item["category"]

            print(f"{most_category} ({most_expense} PKR)")

            # AVERAGE SPENDING
            print("Daily Average Spending:")
            print(f"{int(total_expense/ 30)} PKR/day")

        except ValueError as e:
            print(f"Error: {e}")


    def currency_conversion(self, username, rupees):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            total_expense = 0
            user = self.users[username]
            expenses = user["expenses"]

            if len(expenses) == 0:
                print("No expenses to analyze")
                return

            for expense in expenses:
                total_expense += expense["amount"]

            print("Fetching live exchange rate...")
            print(f"Total Spending: {total_expense} PKR")
            print(f"= {int(total_expense/rupees)} USD (Live)")

            print("Conversion successful!")
        except ValueError as e:
            print(f"Error: {e}")

    def send_email(self, username, receiver):
        try:
            if username not in self.users:
                raise ValueError("User does not exist")

            print("📧 Preparing expense report...")

            user = self.users[username]
            expenses = user["expenses"]
            budget = user["budget"]

            if len(expenses) == 0:
                print("No expenses found!")
                return

            # TOTAL
            total = sum(item["amount"] for item in expenses)

            # CATEGORY BREAKDOWN
            category_dict = {}
            for item in expenses:
                cat = item["category"]
                category_dict[cat] = category_dict.get(cat, 0) + item["amount"]

            category_text = ""
            for cat, amt in category_dict.items():
                category_text += f"- {cat}: {amt} PKR\n"

            # TOP CATEGORY
            top_category = max(category_dict, key=category_dict.get)
            top_text = f"{top_category} ({category_dict[top_category]} PKR)"

            # REMAINING
            remaining = budget - total

            # DAILY AVG
            daily_avg = int(total / 30)

            # REPORT
            report = f"""
    Hello {username},

     Total Spending: {total} PKR
     Budget: {budget} PKR
    Remaining Budget: {remaining} PKR

     Category Breakdown:
    {category_text}

     Most Spent Category:
    {top_text}

     Daily Average Spending:
    {daily_avg} PKR/day

    --------------------------------
    Smart Expense Analyzer 
    """

            print("📧 Sending email...")

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(self.MY_EMAIL, self.MY_PASSWORD)
                connection.sendmail(
                    from_addr=self.MY_EMAIL,
                    to_addrs=receiver,
                    msg=f"Subject: Expense Report \n\n{report}"
                )

            print("✅ Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")


system = ExpenseTracker()

is_on = True

while is_on:
    print("--------SMART EXPENSE ANALYZER--------")
    print("1. Register User")
    print("2. Set Monthly Budget")
    print("3. Add Expense")
    print("4. View Expense")
    print("5. Expense Analytics")
    print("6. Currency Conversion")
    print("7. Send Email Report")
    print("8. Exit")

    try:
        choice = int(input("Enter choice"))

        if choice == 1:
            system.register_user(system.get_username())
        elif choice == 2:
            username = system.get_username()
            budget = int(input("Enter monthly budget (PKR): "))
            if budget < 0:
                print("Budget must be a positive number!")
            system.monthly_budget(username, budget)
        elif choice == 3:
            username = system.get_username()
            category = input("(Food/Transport/Shopping/Bills): ")
            amount = int(input("Enter amount (PKR): "))
            if amount < 0:
                print("Amount must be greater than  0!")
            system.add_expense(username,category,amount)
        elif choice == 4:
            username = system.get_username()
            system.view_expenses(username)
        elif choice == 5:
            username = system.get_username()
            system.expense_analytics(username)

        elif choice == 6:
            url = 'https://v6.exchangerate-api.com/v6/6bab87baa3bd85ee1248eb1b/latest/USD'
            response  = requests.get(url)
            response.raise_for_status()
            data = response.json()
            PKR = data["conversion_rates"]["PKR"]
            username = system.get_username()
            system.currency_conversion(username, PKR)

        elif choice == 7:
            username = system.get_username()
            receiver_email = input("Enter email: ")
            system.send_email(username, receiver_email)

        elif choice == 8:
            print("Exiting...")
            is_on= False

    except:
        print("Please enter choice in Digits")