class AccountNumberGenerator:
    _current_id = 0

    @classmethod
    def generate_ba(cls):
        cls._current_id += 1

        return(f"BA{cls._current_id:03d}")

class BankAccount():

    def __init__(self, name: str, initial_balance: float = 0.0):
        self.name = name
        
        self.account_number = AccountNumberGenerator.generate_ba()

        self.__balance = initial_balance

        self.transactions_log = []

        if initial_balance > 0:
            self.transactions_log.append({"action": "Deposit", "amount": initial_balance})

    def get_balance(self):
        return self.__balance

    def get_transaction_log(self):
        if not self.transactions_log:
            print("No transactions exist.")
        else:
            for i, transaction in enumerate(self.transactions_log,1):
                print(f"{i}: {transaction['action']}, Amount: {transaction['amount']}")

    def deposit(self, amount):
        if amount == 0 or amount < 0:
            print("Deposit amount must be greater than 0.")
            return False

        self.__balance += amount
        self.transactions_log.append({"action": "Deposit", "amount": amount})
        print(f"Deposit of amount: {amount} successful.")

        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than zero to withdraw.")
            return False
        
        if amount > self.__balance:
            print("Cannot withdraw an amount that is greater than your balance.")
            return False

        self.__balance -= amount

        self.transactions_log.append({"action": "Withdraw","amount": amount})
        print(f"Withdrawal of amount: {amount} sucessful.")
        return True

    def show_balance(self):
        current_balance = self.get_balance()
        return print(f"Balance: {current_balance}")

    

    
