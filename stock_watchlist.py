import config
from Robinhood import Robinhood


watchlist = ["TSLA", "AMD"]

my_trader = Robinhood()
logged_in = False
logged_in = my_trader.login(username=config.USERNAME, password=config.PASSWORD, qr_code=config.QR)

i = 0
while i < 6:
	for ticker in watchlist:
		ticker_last_price = my_trader.quote_data(ticker)['last_trade_price']
		print(str(ticker) + " : " + str(ticker_last_price))
	time.sleep(10)
	i = i + 1

my_trader.logout()