import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
         # Simple Stock Price App
         Shown are the stock closing price and volume of selected stocks!
    """)

# define the symbol
#Enter stock
tickerSymbol = st.text_input('Please enter your Ticker: ', 'UBSG.SW')
#tickerSymbol = 'UBSG.SW'
st.write('Your selected stock is ', tickerSymbol)


# get data on this ticket
tickerdata = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerdf = tickerdata.history(period = '1d', start ='2018-05-31', end='2022-05-27')
st.subheader("Ticker data")
st.write(tickerdf)

# 
st.subheader('Map Close')
st.line_chart(tickerdf.Close)

st.subheader('Map Volume')
st.line_chart(tickerdf.Volume)
