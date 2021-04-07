"""class BankAccount:
    def __init__(self,amount):
        self.amount=amount
        self.balance=0

    def deposit(self):
        amount=int(input("enter the amount:"))
        print("amount to be deposited",amount)
        self.balance += amount
        
        pass
    def withdrew(self):
        print("amount to be withdrew",amount)
        self.balance-=amount
        pass 



obj1=BankAccount(amount)
obj1.deposit()
obj1.withdrew()
print("deposited amount:",obj1.deposit())
print("withdraw amount:",obj1.withdrew())"""



class Bank_Account:
    def __init__(self):
        self.balance=0
  
    def deposit(self):
        amount=int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:",amount)
  
    def withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        try:
            if self.balance>=amount:
                self.balance-=amount
                print("You Withdrew:", amount)
            else:
                print("\n Insufficient balance  ")
                pass
  
    def display(self):

        print("\n Net Available Balance=",self.balance)
  

obj1 = Bank_Account()
   
obj1.deposit()
obj1.withdraw()
obj1.display()