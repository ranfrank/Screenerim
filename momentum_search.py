import yfinance as yf
yf.pdr_override()  # Fix for yahoo finance
import requirements_check as rc
import news_analysis as na


def momentum_search(stock):
    rating = 0  # 1 = is momentum, 2 = also is a penny stock
    news_rating = 0
    status = False

    try:

        if rc.is_momentum_trade(stock):
            status = True
            rating = 1
        if rc.is_penny_stock(stock):
            rating += 1
        if status:
            news_rating = na.get_news_rating(stock)
    except Exception as e:
        print(e)
        print("momentum_search - No data on " + stock)

    return stock, status, 'Momentum', rating
