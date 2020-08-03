import os
from dotenv import load_dotenv
import yfinance
from fbprophet import Prophet
import quandl

load_dotenv()
quandl.ApiConfig.api_key = os.getenv('QUANDL_KEY')


msft_obj = yfinance.Ticker('MSFT')
msft_df = msft_obj.history(period='max')

aapl_obj = yfinance.Ticker('AAPL')
aapl_df = aapl_obj.history(period='max')

zacks_msft = quandl.get_table('ZACKS/FC', ticker='MSFT')
zacks_aapl = quandl.get_table('ZACKS/FC', ticker='AAPL')


AAPL = aapl_df.reset_index()[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
m = Prophet()
m.fit(AAPL)


future = m.make_future_dataframe(periods=30)
future.tail()


forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
fig1.show()

fig2 = m.plot_components(forecast)
fig2.show()


from fbprophet.plot import plot_plotly
import plotly.offline as py

fig = plot_plotly(m, forecast)
py.plot(fig)