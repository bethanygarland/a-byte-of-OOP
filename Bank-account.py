class BankAccount:
    interest_rate = 0.5
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, num_deposit):
        self.balance += num_deposit
        return self.balance

    def withdraw(self, num_withdraw):
        self.balance -= num_withdraw
        if num_withdraw > self.balance:
            return "insufficient funds"
        else:
            self.balance -= withdrawal_amount
            return self.balance

# bethany = BankAccount()
# print(bethany.balance)
# print(bethany.deposit(5))
# print(bethany.withdraw(2))

    @classmethod
    def create(cls, balance=0):
        account = cls(balance)
        cls.accounts.append(account)
        return account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total

    @classmethod
    def add_interest(cls):
        for account in cls.accounts:
            return account.balance + (account.balance * cls.interest_rate)


def main():
    bethany = BankAccount.create(200)
    emily = BankAccount.create(150)
    # print(bethany.balance)
    # print(emily.balance)
    # print(emily.withdraw(350))
    # print(emily.deposit(200))
    #
    # print(BankAccount.add_interest())
    # print(bethany.balance)
    print(BankAccount.total_funds())

main()
