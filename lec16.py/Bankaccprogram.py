from bankacc import Bankacc
acc1=Bankacc(101,"Vijay Bansal",10000)
acc2=Bankacc(102,"Sourav Verma",15000)
acc1.deposit=5000
acc1.withdraw=2000
acc2.deposit=2000
acc2.withdraw=3000
acc1.display() 
print("Deposit=",acc1.deposit)
print("Withdraw=",acc1.withdraw)
print("Current Balance =", acc1.getbalance()) 

acc2.display()
print("Deposit=",acc2.deposit)
print("Withdraw=",acc1.withdraw)
print("Current Balance =", acc2.getbalance())

print(f"Total BankAcc instances created: {Bankacc.count}")