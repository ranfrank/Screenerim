from finvizfinance.quote import finvizfinance
from configparser import ConfigParser

m = {'K': 3, 'M': 6, 'B': 9, 'T': 12}

config = ConfigParser()
config.read('py.properties')


def get_fundamentals(ticker):
    return finvizfinance(ticker).TickerFundament()


def is_penny_stock(stock):
    try:
        fundamentals = get_fundamentals(stock)

        shs_float = int(float(fundamentals['Shs Float'][:-1]) * 10 ** m[fundamentals['Shs Float'][-1]])
        if shs_float > float(config.get('PARAMETERS', 'SHS_FLOAT')):
            return False

        market_cap = int(float(fundamentals['Market Cap'][:-1]) * 10 ** m[fundamentals['Market Cap'][-1]])
        if market_cap > float(config.get('PARAMETERS', 'MARKET_CAP')):
            return False

        price = int(float(fundamentals['Price'][:-1]))
        if price > float(config.get('PARAMETERS', 'MAX_PRICE_PENNY')):
            return False

        return True

    except:
        return False


def is_momentum_trade(stock):
    try:
        fundamentals = get_fundamentals(stock)

        avg_vol = int(float(fundamentals['Avg Volume'][:-1]) * 10 ** m[fundamentals['Avg Volume'][-1]])

        if avg_vol < int(config.get('PARAMETERS', 'AVG_VOL')):
            return False
        if float(fundamentals['Change'][:-1]) < float(config.get('PARAMETERS', 'PERCENT_CHANGE')):
            return False
        if float(fundamentals['Rel Volume']) < float(config.get('PARAMETERS', 'REL_VOL')):
            return False

        return True

    except:
        return False
