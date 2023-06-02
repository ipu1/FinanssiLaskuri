transactions = []

def add_transaction():
    name = input("Enter the name of the transaction: ")
    date = input("Enter the date of the transaction (YYYY-MM-DD): ")
    amount = float(input("Enter the amount of the transaction: "))
    transactions.append({"name": name, "date": date, "amount": amount})

def view_transactions():
    for transaction in transactions:
        print(f"{transaction['date']} - {transaction['name']}: {transaction['amount']}")

def search_transactions():
    search_type = input("Search by name or date? ")
    search_query = input(f"Enter the {search_type} to search for: ")

    for transaction in transactions:
        if transaction[search_type] == search_query:
            print(f"{transaction['date']} - {transaction['name']}: {transaction['amount']}")

while True:
    print("1. Add a transaction")
    print("2. View transactions")
    print("3. Search transactions")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        search_transactions()
    elif choice == "4":
        break
