from cyberhead.strategies.strategy import Broker
from pandas import DataFrame

from backtesting.lib import crossover
from backtesting.test import GOOG

broker = Broker()
data = DataFrame

broker.name = 'alpaca'
broker.commission = .002
broker.cash = 10000
broker.prices = GOOG

data.sma_10 = [123, 123, 123]
data.sma_20 = [123, 123, 123]


def iterate(broker, data):
    '''please note that broker, data and iterate are not related here,
    this objects are called by the stratmanager'''

    if crossover(data.sma_10, data.sma_20):
        broker.buy()
    elif crossover(data.sma_20, data.sma_10):
        broker.sell()
