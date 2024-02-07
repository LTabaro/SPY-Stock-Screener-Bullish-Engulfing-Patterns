import yfinance as yf

ticker = "MSFT"

msft = yf.Ticker(ticker)

df = msft.history(period="1y")

print(df.to_csv())



