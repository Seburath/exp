def run_strategies(strategies):
    for strategy in strategies:
        exec(f'''
from cyberhead.strategies.strategies.{strategy} import {strategy}
from backtesting import Backtest, Strategy


class backtest_{strategy}(Strategy):
    def init(self):
        Close = self.data.Close

    def next(self):
        {strategy}.iterate(self, {strategy}.data)


bt = Backtest({strategy}.broker.prices,
            backtest_{strategy},
            cash={strategy}.broker.cash,
            commission={strategy}.broker.commission)


bt.run()
bt.plot()

print('{strategy} backtest performed!')
''', globals())
