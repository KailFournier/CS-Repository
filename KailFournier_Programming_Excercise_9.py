class BankAcct:
    #Class init
    def __init__(self, name, account_number, initial_amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = initial_amount
        self.interest_rate = interest_rate

    def set_i_rate(self, new_rate): #sets the interest rate
        self.interest_rate = new_rate

    def deposit(self, amount): #Deposits money into account
        self.amount += amount

    def withdraw(self, amount): #Withdarws funds from account
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount

    def gbalance(self): #Returns the account balance
        return self.amount

    def cinterest(self, days): #notates the interest rate
        return (self.interest_rate * days / 365) * self.amount

    def __str__(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.amount:.2f}, Interest Rate: {self.interest_rate:.2%}"

def test_bank_account(dep, dep2, wit, wit2,intrd, intr):
    acct = BankAcct("Kail Fournier", "12345", 1825.0, 0.1)
    print(acct)
    print("Depositing: ", dep)
    acct.deposit(dep)
    print("After deposit:", acct.gbalance())
    print("Withdrawing: ", wit)
    acct.withdraw(wit)
    print("After withdrawal:", acct.gbalance())
    print("Withdrawing: ", wit2)
    acct.withdraw(wit2)  # should print insufficient funds
    print("Depositing: ", dep2)
    acct.deposit(dep2)
    print("After deposit:", acct.gbalance())
    interest = acct.cinterest(intrd)
    print(f"Interest for {intrd}  days, {interest:.2f}")
    print("Setting interest rate to: ", intr)
    acct.set_i_rate(intr)
    print("After changing interest rate:", acct)

test_bank_account(150, 200, 1800, 1000, 30, .02 )