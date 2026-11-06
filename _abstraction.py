from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self):
        pass


class PayPal(PaymentGateway):

    def pay(self):
        print("paying using Paypal...")


class TeluskoPay(PaymentGateway):

    def pay(self):
        print("paying using Telusko...")


class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("checking out")
        self.gateway.pay()

purchase = Purchase(PayPal())
purchase.checkout()