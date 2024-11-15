import csv

TRANSACTION_FILE = "transactions.csv"

def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    amount = float(input("Enter the amount (positive for income, negative for expense): "))
    
    with open(TRANSACTION_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    
    print("Transaction added successfully!")

def display_transactions():
    total_income = 0
    total_expense = 0

    print("\n--- All Transactions ---")
    print(f"{'Date':<15}{'Description':<25}{'Amount':<10}")
    print("-" * 50)
    
    try:
        with open(TRANSACTION_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                date, description, amount = row
                amount = float(amount)
                
                if amount > 0:
                    total_income += amount
                else:
                    total_expense += abs(amount)
                
                print(f"{date:<15}{description:<25}{amount:<10.2f}")
    except FileNotFoundError:
        print("No transactions found.")

    print("\n--- Summary ---")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expense:.2f}")
    print(f"Remaining Budget: {total_income - total_expense:.2f}")

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            display_transactions()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
