'''BankAcc - Properties - accNo, accName, balance, constructor, deposit, withdraw, display, getbalance'''
class Bankacc:
    count=0
    def __init__(self,accNo, accName, balance):
        print("BankAcc constructor called")
        self.accNo=accNo
        self.accName=accName
        self.balance=balance
        Bankacc.count+=1
        self.id=Bankacc.count 
    def display(self):
        print("Account Number :", self.accNo)
        print("Account Holder :", self.accName)
        print("Balance :", self.balance)
    def deposit(self,amount):
        self.balance=self.balance + amount
        print("Amount deposited=",amount)
    def withdrawn(self,amount):
        self.balance=self.balance + amount
        print("Amount withdrawn=",amount)
    def getbalance(self):
        return self.balance