class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount} into account {self.account_number}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount} from account {self.account_number}. New balance: ₹{self.balance}")

class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Added interest ₹{interest} to account {self.account_number}. New balance: ₹{self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, product_type):
        super().__init__(account_number, account_holder, balance)
        self.product_type = product_type

    def check_balance_requirement(self):
        if self.product_type == "Premium Banking Program":
            if self.balance < 500000:
                print("Balance requirement not met. Minimum balance required: ₹5,00,000")
            else:
                print("Balance requirement met.")
        elif self.product_type == "Zero2One Program":
            if self.balance < 100000:
                print("Balance requirement not met. Minimum balance required: ₹1,00,000 (Waiver for first 3 years)")
            else:
                print("Balance requirement met.")

saving_account = SavingAccount("SAV123", "John Doe", 10000, 2)
saving_account.deposit(5000)
saving_account.add_interest()

current_account1 = CurrentAccount("CUR123", "ABC Corporation", 500000, "Premium Banking Program")
current_account1.check_balance_requirement()

current_account2 = CurrentAccount("CUR456", "StartupX", 50000, "Zero2One Program")
current_account2.check_balance_requirement()