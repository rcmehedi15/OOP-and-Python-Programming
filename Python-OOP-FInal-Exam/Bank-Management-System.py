import random

class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_bank_balance = 0
        self.loan_feature_on = True
        self.total_loan_amount = 0

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        self.accounts[account_number] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transactions': [],
            'loans_taken': 0
        }
        return account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            self.total_bank_balance -= self.accounts[account_number]['balance']
            del self.accounts[account_number]
            return True
        return False

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['transactions'].append(('Deposit', amount))
            self.total_bank_balance += amount
            return True
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number]['balance'] >= amount:
            self.accounts[account_number]['balance'] -= amount
            self.accounts[account_number]['transactions'].append(('Withdrawal', amount))
            self.total_bank_balance -= amount
            return True
        elif self.total_bank_balance < amount:
            return "Bank is bankrupt"
        return "Withdrawal amount exceeded"

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        return "Account does not exist"

    def transaction_history(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['transactions']
        return "Account does not exist"

    def transfer(self, from_acc, to_acc, amount):
        if to_acc not in self.accounts:
            return "Account does not exist"
        if from_acc in self.accounts and self.accounts[from_acc]['balance'] >= amount:
            self.withdraw(from_acc, amount)
            self.deposit(to_acc, amount)
            return True
        return "Insufficient funds"

    def list_accounts(self):
        return [(acc, acc_details['name'], acc_details['balance']) for acc, acc_details in self.accounts.items()]

    def total_balance(self):
        return self.total_bank_balance

    def loan(self, account_number, amount):
        if not self.loan_feature_on or self.accounts[account_number]['loans_taken'] >= 2:
            return False
        self.accounts[account_number]['balance'] += amount
        self.accounts[account_number]['transactions'].append(('Loan', amount))
        self.accounts[account_number]['loans_taken'] += 1
        self.total_loan_amount += amount
        self.total_bank_balance += amount
        return True

    def toggle_loan_feature(self, status):
        self.loan_feature_on = status
        return self.loan_feature_on

def user_interface(bank):
    while True:
        print("\nUser Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Check Transaction History")
        print("6. Take a Loan")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to deposit: "))
            if bank.deposit(acc_num, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Account not found.")
        elif choice == '2':
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to withdraw: "))
            result = bank.withdraw(acc_num, amount)
            if result == True:
                print("Withdrawal successful.")
            else:
                print(result)
        elif choice == '3':
            acc_num = int(input("Enter your account number: "))
            result = bank.check_balance(acc_num)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Your current balance is: ${result:.2f}")
        elif choice == '4':
            from_acc = int(input("Enter your account number: "))
            to_acc = int(input("Enter the account number to transfer to: "))
            amount = float(input("Enter the amount to transfer: "))
            result = bank.transfer(from_acc, to_acc, amount)
            if result == True:
                print("Transfer successful.")
            else:
                print(result)
        elif choice == '5':
            acc_num = int(input("Enter your account number: "))
            history = bank.transaction_history(acc_num)
            if isinstance(history, str):
                print(history)
            else:
                for transaction in history:
                    print(f"{transaction[0]} of ${transaction[1]:.2f}")
        elif choice == '6':
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter the loan amount: "))
            if bank.loan(acc_num, amount):
                print("Loan granted successfully.")
            else:
                print("Loan cannot be processed. Either loan feature is off or loan limit reached.")
        elif choice == '7':
            break
        else:
            print("Invalid option, please try again.")

def admin_interface(bank):
    while True:
        print("\nAdmin Menu")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List All Accounts")
        print("4. Check Total Bank Balance")
        print("5. Toggle Loan Feature")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully! Account number: {account_number}")
        elif choice == '2':
            acc_num = int(input("Enter the account number to delete: "))
            if bank.delete_account(acc_num):
                print("Account deleted successfully.")
            else:
                print("Account not found.")
        elif choice == '3':
            accounts = bank.list_accounts()
            print("List of all accounts:")
            for acc in accounts:
                print(f"Account Number: {acc[0]}, Name: {acc[1]}, Balance: ${acc[2]:.2f}")
        elif choice == '4':
            print(f"Total bank balance: ${bank.total_balance():.2f}")
        elif choice == '5':
            status = input("Enable loan feature? (yes/no): ").lower() == 'yes'
            bank.toggle_loan_feature(status)
            print("Loan feature updated successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Banking System")
        role = input("Are you a user or an admin? (user/admin): ")
        if role.lower() == 'user':
            user_interface(bank)
        elif role.lower() == 'admin':
            admin_interface(bank)
        else:
            print("Invalid role selected. Please enter 'user' or 'admin'.")

if __name__ == "__main__":
    main()
