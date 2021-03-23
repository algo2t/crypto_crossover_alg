import os
from cbpro import *
from dotenv import load_dotenv
load_dotenv()


class Account:
    """ Authenticates, checks balances, places orders. """

    def __init__(self):
        self.auth_client = AuthenticatedClient(os.getenv("api_key"), os.getenv("secret"), os.getenv("passphrase"))
        self.account = self.auth_client.get_accounts()
        self.size = 0.0001

    def buy(self):
        return self.auth_client.place_market_order(
            'BTC-USD',
            'buy',
            size=self.size
        )

    def sell(self):
        return self.auth_client.place_market_order(
            'BTC-USD',
            'sell',
            size=self.size
        )