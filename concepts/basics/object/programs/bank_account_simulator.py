class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def displayAccountDetails(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        self.currentBalance();
        
    def deposit(self, amt):
        if amt <= 0:
            print("Invalid amount!")
        else:
            self.balance += amt
            print(f"$ {amt} has been added to your account. New balance: ${self.balance:.2f}\n")
    
    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid amount!")
        elif amt > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amt
            print(f"Successfully withdrawed ${amt:.2f}. New balance: ${self.balance: .2f}")
            
    def currentBalance(self):
        print(f"Current balance: ${self.balance: .2f}")

person1 = BankAccount("19103991", "Shannen Nazareno", 1000)

person1.displayAccountDetails()
person1.deposit(1)
person1.withdraw(2000)
person1.withdraw(1001)