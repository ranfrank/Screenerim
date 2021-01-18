import yfinance as yf
yf.pdr_override()  # Fix for yahoo finance


def deadCat_search(stock):
    rating = 0
    status = False

    ticker = yf.Ticker(stock)
    hist = ticker.history(period='1w', interval='1d')

    # TODO write the criteria

    return status, 'Dead Cat', rating
