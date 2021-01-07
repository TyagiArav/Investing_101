import streamlit as st
import yfinance as yf

selections = ("GOOGL", "APPL", "AMZN")
tickerSymbol = st.selectbox(selections)

tickerdata = yf.Ticker(tickerSymbol)

tickerDf = tickerdata.history(period='1d', start='2020-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
'Web app Still in progress'
'More to come!'
