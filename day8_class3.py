class BankAccount:
    def __init__(self, account_holder,balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def withdraw(self, withdraw_amt):
        self.withdraw_amt = withdraw_amt
        self.deposit(0)
        print(self.balance)
        print(self.withdraw_amt)
        if self.withdraw_amt <= self.balance:
            self.balance = self.balance - self.withdraw_amt
        else:
            print("Insufficeint Balance")
    def display_balance(self):
        print(self.balance)
    
cust1 = BankAccount("Kannan", 30000)
cust1.deposit(20000)
cust1.withdraw(300)
cust1.display_balance()

#stud1 = Student("Vihan", 30, [8,7,9,55])

#print("Student Pass :", stud1.is_passing())


