import streamlit as st
import yfinance as yf
import pandas as pd

df = pd.DataFrame({
  'stock': ["GOOGL", "AAPL", "AMZN"],
})
tickerSymbol = st.selectbox("What is the stock your looking for", df['stock'])
tickerdata = yf.Ticker(tickerSymbol)

tickerDf = tickerdata.history(period='1d', start='2020-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
