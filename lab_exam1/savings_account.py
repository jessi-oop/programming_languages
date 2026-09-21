from bank_account import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, name,  interest_rate, minimum_balance, initial_balance = 0):
        super().__init__(name, initial_balance)

        self.interest_rate = interest_rate / 100
        self.minimum_balance = minimum_balance


    def add_interest(self):
        current_balance = self.get_balance()

        interest_gained = current_balance * self.interest_rate

        if interest_gained > 0:
            self.deposit(interest_gained)
            print(f"Interest gained: {interest_gained}")

        return interest_gained

    def withdraw(self, amount):
        current_balance = self.get_balance()

        if (current_balance - amount) < self.minimum_balance:
            print(f"Failed to withdraw. Withdrawal will make the balance less than the minimum balance of {self.minimum_balance}.")
            return False

        return super().withdraw(amount)

    


        

