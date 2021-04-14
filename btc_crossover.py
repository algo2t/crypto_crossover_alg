import time
import logging
from datetime import datetime
from Account import Account
from History import History


def run():
    logging.basicConfig(filename='log.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.DEBUG)
    logging.info('Initiating Run')
    auth_client = Account()
    history = History('BTC-USD')
    sma50 = history.sma(50)
    sma100 = history.sma(100)
    if sma50 > sma100:
        bull_flag = True
    else:
        bull_flag = False
    while True:
        if datetime.now().minute == 0:
            history = History('BTC-USD')
            if bull_flag is False and history.sma(50) > history.sma(100):
                buy = auth_client.buy('BTC-USD')
                logging.info(f'Golden Cross: {buy}')
                bull_flag = True
            if bull_flag is True and history.sma(50) < history.sma(100):
                sell = auth_client.sell('BTC-USD')
                logging.info(f'Death Cross: {sell}')
                bull_flag = False
            else:
                logging.info('No Crossover event')
            time.sleep((60 * 60) - datetime.now().minute * 60 - (datetime.now().microsecond / 1000000))
        else:
            time.sleep((60 * 60) - datetime.now().minute * 60 - (datetime.now().microsecond / 1000000))


if __name__ == '__main__':
    run()
