class bankaccount:
    def __init__(self, name, pin, balance=0):
        self.name = name 
        self.pin = pin 
        self.balance = balance 
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"deposited ${amount}")
        print(f"${amount} deposited! new balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"withdraw ${amount}")
            print(f"${amount} withdraw! new balance: ${self.balance}")
        else:
            print("insufficient balance!")
    
    def show_balance(self):
        print(f"account holder: {self.name}, balance: ${self.balance}")
    
    def show_history(self):
        print("\n--transaction history--")
        if self.history:
            for t in self.history:
                print(t)
        else:
            print("no transactions yet!")


# Main program
if __name__ == "__main__":
    name = input("enter your name: ")
    pin = input("set a 4-digit PIN: ")
    account = bankaccount(name, pin)
    
    if input("enter PIN to login: ") != account.pin:
        print("wrong pin! access denied.")
        exit()
    
    while True:
        print("\n1.deposit 2.withdraw 3.show balance 4.history 5.exit")
        choice = input("choose: ")
        
        if choice == "1":
            account.deposit(int(input("enter amount: ")))
        elif choice == "2":
            account.withdraw(int(input("enter amount: ")))
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            account.show_history()
        elif choice == "5":
            print("goodbye!")
            break
        else:
            print("invalid choice!")
                                