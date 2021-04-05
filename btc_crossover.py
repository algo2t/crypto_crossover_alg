import time
from datetime import datetime
from Account import Account
from History import History


def run():
    print('initiating run()')
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
                print("Golden Cross, trigger buy")
                buy = auth_client.buy('BTC-USD')
                print(datetime.now(), buy)
                bull_flag = True
            if bull_flag is True and history.sma(50) < history.sma(100):
                print("Death Cross, trigger sell")
                sell = auth_client.sell('BTC-USD')
                print(datetime.now(), sell)
                bull_flag = False
            else:
                print(datetime.now())
                print("No crossover event.")
            time.sleep((60 * 60) - datetime.now().minute * 60 - (datetime.now().microsecond / 1000000))
        else:
            time.sleep((60 * 60) - datetime.now().minute * 60 - (datetime.now().microsecond / 1000000))


if __name__ == '__main__':
    run()
