class Account:
    def __init__(self, owner, balance=0):
     self.owner = owner                 
     self.__balance = balance          

    def deposit(self, amount):
      if amount > 0:
        self.__balance += amount
        print(f"${amount} deposited.")
      else:
        print("Deposit amount must be positive.")

    def withdraw(self, amount):
       if 0 < amount <= self.__balance:
        self.__balance -= amount
        print(f"${amount} withdrawn.")
       else:
         print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance
  

account = Account("James", 100)

print(account.owner)                 

account.deposit(50)                   
print(account.get_balance())          
account.withdraw(75)                  
print(account.get_balance())          
