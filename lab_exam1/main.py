from checking_account import CheckingAccount
from savings_account import SavingsAccount

class InputValidator:
    @staticmethod
    def get_float(user_input: str):
        while True:
            try:
                value  = float(input(user_input))
                return value
            except ValueError:
                print("Error: Please print a valid number.")

    @staticmethod
    def get_int(user_input: str):
        while True:
            try:
                value = int(input(user_input))
                return value
            except ValueError:
                print("Error: Please enter a whole number.")

def main(input_validator = InputValidator):
    bank_db = {}

    print("--------Welcome to my bank anjing ya---------")
    while True:
        print("\n------Choose an action-------")

        print("[1] Create account")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Check balance")
        print("[5] Add interest (savings only)")
        print("[6] View transaction history")
        print("7 Exit")
        action = input_validator().get_int("Enter your chosen action (1-7): ")
       
        if action == 1:
            print("Choose what type of account to create.")
            print("[1] Savings Account")
            print("[2] Checking Account")
            account_type = input_validator.get_int("Enter your chose action (1-2): ")
            if account_type == 1 and account_type == 2:
                print("Please enter a valid option (1-2)")
                continue

            name = str(input("Enter account holder name: ")).strip()


            if account_type == 1:
                interest_rate = input_validator().get_float("Enter interest rate (this will be converted to percentage): ")
                if interest_rate < 0:
                    print("Error. Value must be a real amount and a positive value.")
                    continue
                
                minimum_balance = input_validator().get_float("Enter minimum balance for this account: ")
                if minimum_balance < 0:
                    print("Error.Amount must be greater than 0.")
                    continue

                initial_balance = input_validator.get_float("Please deposit initial balance for this account (amount must be greater than minimum balance): ")
                if initial_balance < 0:
                    print("Error. Amount must be greater than 0.")
                    continue
                 
                if initial_balance < minimum_balance:
                    print("Initial balance must be greater thatn minimum balance.")
                    continue
                
                new_account  = SavingsAccount(name, interest_rate, minimum_balance, initial_balance)
                bank_db[new_account.account_number] = new_account
                print(f"Account created successfully! Your bank account number is: {new_account.account_number}")

            elif account_type == 2:
                initial_balance = input_validator.get_float("Please deposit an initial balance: ")
                if initial_balance < 0:
                    print("Error.Amount must be greater than 0.")
                    
                new_account = CheckingAccount(name, initial_balance)
                bank_db[new_account.account_number] = new_account
                print(f"Account created successfully! Your account number is {new_account.account_number}")

        elif action == 2:
            print("----Deposit----")

            account_number = input("Enter account number: ")

            if account_number in bank_db:
                current_account = bank_db[account_number]

                amount = input_validator().get_float("Enter amount to deposit: ")
                current_account.deposit(amount)
            else:
                print("Error: Account not found.")
                continue

        elif action == 3:
            print("----Withdraw----")
            account_number = input("Enter account number: ")

            if account_number in bank_db:
                current_account = bank_db[account_number]

                amount = input_validator().get_float("Enter amount to withdraw: ")

                current_account.withdraw(amount)
            else:
                print("Error. Account not found.")

        elif action == 4:
            print("----Check Balance----")
            account_number = input("Enter account number: ")

            if account_number in bank_db:
                current_account = bank_db[account_number]

                current_account.show_balance()
            else:
                print("Error. Account not found.")

        elif action == 5:
            print("----Add Interest----")
            account_number = input("Enter account number: ")

            if account_number in bank_db:
                current_account = bank_db[account_number]

                if isinstance(current_account, SavingsAccount):
                    current_account.add_interest()
                else:
                    print("Invalid action. This action are for savings account only.")
            else:
                print("Error. Account not found.")

        elif action == 6:
            print("----Transaction History----")

            account_number = input("Enter account number: ")

            if account_number in bank_db:
                current_account = bank_db[account_number]

                print(f"----Transaction history for: {current_account.name}----")
                current_account.get_transaction_log()
            else:
                print("Error. Account not found.")

        elif action == 7:
            print("Thanks for using our bank anjing ya!")
            break
        else:
            print("Ooppsie. That options is not on the list. Please try again.")

if __name__ == "__main__":
    main()
        