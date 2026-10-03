from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class CashPayment (Payment):
    def pay(self):
        print("Paid using cash")

class CardPayment (Payment):
    def pay(self):
        print("Paid using card")

cash_pay=CashPayment()
cash_pay.pay()
card_pay=CardPayment()
card_pay.pay()