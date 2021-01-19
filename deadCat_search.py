import yfinance as yf
yf.pdr_override()  # Fix for yahoo finance


def deadCat_search(stock):
    rating = 1
    status = False
    up_percentage = 20
    down_percentage = -5

    ticker = yf.Ticker(stock)
    hist = ticker.history(period='7d', interval='1d')

    hist['Percent Change'] = hist['Close'].pct_change()
    # stock_return = hist['Percent Change'].sum() * 100
    try:
        if ( (hist['Percent Change'][-3] > up_percentage or hist['Percent Change'][-2] > up_percentage) and
                (hist['Percent Change'][-2] < down_percentage or hist['Percent Change'][-1] < down_percentage)):
            status = True
    except Exception as e:
        print(e)
        print("deadCat_search - No data on " + stock)

    return stock, status, 'Dead Cat', rating
