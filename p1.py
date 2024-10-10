class bankaccount:
    interestrate = 6.5
    
    def __init__(self,accountnumber,name,deposit):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = deposit
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. and New Balance: {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!!")
        else:
            self.balance -=amount
            print(f"Withdraw {amount}. New Balance: {self.balance}")
    
    def checkbalance(self):
        return self.balance
    
    def __str__(self):
        return f"Account: {self.accountnumber}, Name: {self.name}, Balance: {self.balance}"
    
class AccountManagement:
    def __init__(self):
        self.accounts = {}
    
    def addaccount(self,account):
        self.accounts[account.accountnumber] = account
        print(f"Account {account.accountnumber} added.")
        
    def deleteaccount(self,accountnumber):
        if accountnumber in self.accounts:
            del self.accounts[accountnumber]
            print(f"Account {accountnumber} Deleted.")
        else:
            print(f"Account Not Found.")
    
    def updateaccount(self,accountnumber,name=None,deposit=None):
        if accountnumber in self.accounts:
            account = self.accounts[accountnumber]
            if name:
                account.name = name
                print(f"Account {accountnumber} name updated to {name}.")
            if deposit is not None:
                account.deposit(deposit)
        else:
            print("Account Not Found.")
    
    def getaccount(self,accountnumber):
        return self.accounts.get(accountnumber,None)

class Bank(bankaccount,AccountManagement):
    def __init__(self):
        AccountManagement.__init__(self)

bank = Bank()

account1 = bankaccount('1002563','Krishna',10000)
account2 = bankaccount('1125687','Sunny',80000)

bank.addaccount(account1)
bank.addaccount(account2)

print(account1.checkbalance())
print(account2.checkbalance())

account1.deposit(1000)
account2.deposit(2500)

bank.updateaccount('1002563',name="Dhruvin",deposit=2500)
bank.deleteaccount('456')

account = bank.getaccount('1002563')
if account:
    print(account)