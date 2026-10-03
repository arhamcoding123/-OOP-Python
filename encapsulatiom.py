class BankAccount:
    def __init__(self,owner,pin,balance):
        self.owner=owner
        self._pin=pin
        self.___balance=balance
    def get_balance(self):
        return self.___balance

my_account= BankAccount("Arham",234,1000000000000)

print(f"Account Name:{my_account.owner}")
print(f"Pin:{my_account._pin}")
print(f"Balance:{my_account.get_balance()}TK")