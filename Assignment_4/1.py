class BankAccount():
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number;
        self.owner_name = owner_name;
        self.balance = balance;
    
    def deposite(self, deposite_amount):
        self.balance = self.balance + deposite_amount;
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Insufficient Balance");
        else:
            self.balance = self.balance - withdraw_amount;

    def checkbalance(self):
        print(f"The Balance in the account is: {self.balance}");

account1 = BankAccount("32039822566", "Radhika", 800);
account1.deposite(200);
account1.withdraw(4000);
account1.withdraw(400);
account1.checkbalance();