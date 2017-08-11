# wallet.py


class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        # defaults to 0 if no initial_amount is specified
        self.balance = initial_amount

    def spend_cash(self, amount):
        # check to see if sufficient amount already exists
        if self.balance < amount:
            raise InsufficientAmount(
                'Not enough available to spend {}'.format(amount))

        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
