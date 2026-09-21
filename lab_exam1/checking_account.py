from bank_account import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, name, initial_balance = 0):
        super().__init__(name, initial_balance)

        self.withdrawal_fee = 1.50

    def withdraw(self, amount):
        current_balance = self.get_balance()

        total_amount = amount + self.withdrawal_fee

        return super().withdraw(total_amount)