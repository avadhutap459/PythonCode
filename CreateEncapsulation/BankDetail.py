class BankAccount:
    def __init__(self,accountnumber,balance):
        self._accountno = accountnumber
        self._balance = balance
    
    def Deposite(self,amount):
        self._balance += amount
        print("You current account balance is :" , self._balance)
    
    def Withdraw(self,amount):
        self._balance -= amount
        print("You current account balance is :" , self._balance)

class SavingAccount(BankAccount):
    def __init__(self, accountnumber, balance):
        super().__init__(accountnumber, balance)
    
    def InterestOnSavingAccount(self):
        rateOfIn = (self._balance / 100) * 6
        self._balance += rateOfIn
        print("You will get interest on your account : ", self._balance)

class CurrentAccount(BankAccount):
    def __init__(self, accountnumber, balance):
            super().__init__(accountnumber, balance)
        
    def InterestOnCurrentAccount(self):
        rateOfIn = 0
        self._balance += rateOfIn
        print("You will get interest on your account : ", self._balance)



s = SavingAccount(123456789,100)
s.Deposite(100)
s.InterestOnSavingAccount()
