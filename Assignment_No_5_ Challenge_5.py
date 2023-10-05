### Challenge 5: Handling a Bank Account

class Account:

    def __init__(self, title = None, Balance = 0):
        self.title = title
        self.Balance = Balance
    
    def withdrawal(self, amount):
        if amount <= self.Balance and amount > 0:
            self.Balance -= amount
        else:
            print("Insufficient balance in your Account.")

    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
        else:
            print("Invalid deposit amount.")
        
    def getBalance(self):
        return self.Balance

class SavingsAccount(Account):

    def __init__(self,title = None, Balance = 0, interestRate = 0):
        super().__init__(title, Balance)
        self.interestRate = interestRate

    def interestAmount(self):
        interest_Amount = (self.interestRate * self.Balance) / 100
        return interest_Amount

demo1 = SavingsAccount("Ashish", 2000, 5)
print("Title : ",demo1.title)
print("Balance : ",demo1.Balance)
print("InterestRate : ", demo1.interestRate)

## Deposit - 500
demo1.deposit(500)
print("After deposite 500 getBalance : ", demo1.getBalance())
print()


## Withdrawal - 500
print("Now Account Balance is : ",demo1.Balance)
demo1.withdrawal(500)
print("After withdrawal 500 getBalance : ", demo1.getBalance())


##interest_Amount
print()
print(f"interest_Amount for {demo1.Balance}  is : ",demo1.interestAmount())



##### Thank You.....       

