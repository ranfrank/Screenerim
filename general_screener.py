from pandas_datareader import data as pdr
from yahoo_fin import stock_info as si
from pandas import ExcelWriter
import yfinance as yf
import pandas as pd
from daily_search import daily_search
from falseBreakout_search import false_breakout_search
from deadCat_search import deadCat_search

yf.pdr_override()

stocklist = si.tickers_nasdaq()
index_name = '^GSPC'  # S&P 500

exportList = pd.DataFrame(columns=['Stock', 'Strategy', 'Rating'])

for stock in stocklist[0:50]:

    deadCat_results = deadCat_search(stock)
    if (deadCat_results[0]):
        exportList = exportList.append(
            {'Stock': stock, 'Strategy': deadCat_results[1], 'Rating': deadCat_results[2]}, ignore_index=True)

    engulfing_result = false_breakout_search(stock)
    if (engulfing_result[0]):
        exportList = exportList.append(
            {'Stock': stock, 'Strategy': engulfing_result[1], 'Rating': engulfing_result[2]}, ignore_index=True)

print(exportList)

writer = ExcelWriter("ScreenOutput.xlsx")
exportList.to_excel(writer, "Sheet1")
writer.save()
