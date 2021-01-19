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
search_results = []

# Search for all strategies
for stock in stocklist[0:300]:
    search_results.append(deadCat_search(stock))
    search_results.append(false_breakout_search(stock))

# Create list with relevant stocks
for result in search_results:
    if result[1]:
        exportList = exportList.append(
            {'Stock': result[0], 'Strategy': result[2], 'Rating': result[3]}, ignore_index=True)
        print(result[0] + ' is match for ' + result[2])

print(exportList)

# Generate result file
writer = ExcelWriter("ScreenOutput.xlsx")
exportList.to_excel(writer, "Sheet1")
writer.save()
