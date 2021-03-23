from cbpro import *
from datetime import datetime, timedelta
import numpy as np


class History():
    """ Gets data and returns signal. """

    def __init__(self, coin=None):
        self.pc = PublicClient()
        self.avg1 = 50
        self.avg2 = 100
        self.start_date = None
        self.end_date = None
        self.data = None
        self.coin = coin

    def sma(self, time_frame):
        """Returns the simple moving average price of bitcoin for the time frame provided in hours."""
        self.start_date = (datetime.now() - timedelta(seconds=60 * 60 * 200)).strftime("%Y-%m-%dT%H:%M")
        self.end_date = datetime.now().strftime("%Y-%m-%dT%H:%M")

        self.data = self.pc.get_product_historic_rates(
            self.coin,
            start=self.start_date,
            end=self.end_date,
            granularity=3600
        )

        self.data.sort(key=lambda x: x[0])

        return np.mean([x[4] for x in self.data[-time_frame:]])