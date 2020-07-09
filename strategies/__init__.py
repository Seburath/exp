from os import system
from cyberhead.strategies.stratmanager import run_strategies


def start():
    strategies = ['strat1', 'strat2']
    run_strategies(strategies)
    return 'Strategies initilized!', 15
