import yfinance as yf
yf.pdr_override()  # Fix for yahoo finance


def false_breakout_search(stock):
    rating = 0

    ticker = yf.Ticker(stock)
    hist = ticker.history(period='3d', interval='1d')

    try:
        if hist['Low'].size >= 2 and hist['High'].size >= 2 and hist['Close'].size >= 2:
            if hist['Low'][-1] < hist['Low'][-2] and hist['Close'][-1] >= hist['High'][-2]:
                rating = 3  # Engulfing
            elif hist['Low'][-1] < hist['Low'][-2] and hist['Close'][-1] >= hist['Close'][-2]:
                rating = 2  # Support
            elif hist['Low'][-1] < hist['Low'][-2] and hist['Close'][-1] >= hist['Low'][-2]:
                rating = 1  # All
    except Exception as e:
        print(e)
        print("false_breakout_search - No data on " + stock)

    return stock, rating > 0, 'False Breakout', rating
